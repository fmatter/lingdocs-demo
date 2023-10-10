.PHONY: cldf

all: load data build cldf

data:
	python3 create_cldf.py
	
load:
	cp /home/florianm/Dropbox/research/cariban/yawarana/yawarana-pld-sketch/cariban.bib sources.bib

build:
	cd doc; pylingdocs build

cldf:
	cd doc; pylingdocs cldf
