from pathlib import Path

import cldf_ldd
import pandas as pd
import pybtex
from cldf_ldd.components import tables as ldd_tables
from pylingdocs.cldf import tables as pld_tables
from cldfbench import CLDFSpec
from cldfbench.cldf import CLDFWriter
from clldutils import jsonlib
from pycldf.dataset import MD_SUFFIX
from pycldf.sources import Source
from pycldf.util import pkg_path


def cread(tablename):
    return pd.read_csv(
        tablename, keep_default_na=False, dtype=str
    )  # no <na>, read everything as strings


def splitcol(
    df, col, sep="; "
):  # split a column (like 'Gloss') by a separator (like ' ')
    df[col] = df[col].apply(lambda x: x.split(sep))


def copycol(df, col1, col2, joiner=None):
    if joiner:
        df[col2] = df[col1].apply(lambda x: joiner.join(x))
    else:
        df[col2] = df[col1]


def parse_param(df):
    splitcol(df, "Parameter_ID")
    copycol(df, "Parameter_ID", "Description", ", ")


spec = CLDFSpec(
    dir="cldf", module="Generic", metadata_fname="metadata.json"
)  # empty cldf specification (https://github.com/cldf/cldf/blob/master/modules/Generic/Generic-metadata.json)
with CLDFWriter(spec) as writer:

    # mapping e.g. "examples.csv" to e.g. "ExampleTable", to use add_component("ExampleTable") later
    cldf_names = {}
    for component_filename in pkg_path(
        "components"
    ).iterdir():  # .../.../pycldf/components/Example-Metadata.json
        component = jsonlib.load(component_filename)  # {"url": "examples.csv", ...}
        cldf_names[component["url"]] = str(component_filename.name).replace(
            MD_SUFFIX, ""
        )  # "examples.csv": Example

    # mapping columns to required table transformation workflows
    table_actions = {
        "Source": lambda x: splitcol(x, "Source"),
        "Gloss": lambda x: splitcol(x, "Gloss", sep=" "),
        "Analyzed_Word": lambda x: splitcol(x, "Analyzed_Word", sep=" "),
        "Parameter_ID": lambda x: parse_param(x),
        "Segments": lambda x: splitcol(x, "Segments", sep=" "),
        "Alignment": lambda x: splitcol(x, "Alignment", sep=" "),
    }

    local_table_files = {}

    for tablename in Path("raw").glob("*.csv"):  # examples.csv
        df = cread(tablename)  # ID  Language_ID Primary_Text
        for col in df.columns:  # apply mapped methods to dataframe
            if col in table_actions:  # Gloss
                table_actions[col](df)  # splitcol(df, "Gloss", sep=" ")
        local_table_files[str(tablename)] = df  # key "examples.csv" holds dataframe
        if str(tablename) == "forms.csv":
            df["Parameter_ID"] = df["Parameter_ID"].apply(lambda x: ", ".join(x))
    for table in ldd_tables + pld_tables:  # morphs.csv
        if table["url"] in local_table_files:
            writer.cldf.add_component(table)  # add json metadata for MorphTable
            for rec in local_table_files.pop(table["url"]).to_dict(
                "records"
            ):  # remove processed cldf-ldd files, iterate rows
                writer.objects[table["url"]].append(rec)  # write row to CLDF

    # now only native CLDF components should be left over
    for key, df in local_table_files.items():  # examples.csv
        if key not in cldf_names:
            print(key)
            continue
        writer.cldf.add_component(
            cldf_names[key]
        )  # add json metadata for "ExampleTable"
        if key == "examples.csv":
            writer.cldf.add_columns(
                "ExampleTable",
                {
                    "name": "Source",
                    "required": False,
                    "propertyUrl": "http://cldf.clld.org/v1.0/terms.rdf#source",
                    "datatype": {"base": "string"},
                    "separator": ";",
                },
            )
        for rec in df.to_dict("records"):
            writer.objects[key].append(rec)

    cldf_ldd.add_columns(writer.cldf)  # add cldf-ldd columns to native tables
    cldf_ldd.add_keys(writer.cldf)  # write cldf-ldd specific keys

    if Path("raw/sources.bib").is_file():  # add sources
        bib = pybtex.database.parse_file(
            "raw/sources.bib",
        )
    writer.cldf.add_sources(*[Source.from_entry(k, e) for k, e in bib.entries.items()])

    ds = writer.cldf

ds.validate()
