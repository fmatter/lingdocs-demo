# Pylingdocs: A Demo

1.  [Introduction](#introduction)
2.  [Common markdown](#common-markdown)
3.  [Pylingdocs markdown](#pylingdocs-markdown)
4.  [Other linguistic data](#other-linguistic-data)
    1.  [Native CLDF components](#native-cldf-components)
    2.  [Non-native components](#non-native-components)
5.  [Interlinear examples](#interlinear-examples)
    1.  [Manual examples](#manual-examples)
6.  [Citing literature](#citing-literature)
7.  [References](#references)

# Introduction

This document does double service as a test for `pylingdocs` and a
showcase of its capabilities. It aims to demonstrate every feature and
model currently available in `pylingdocs`.

# Common markdown

You can use all the familiar markdown components. Here is a link to the
[pylingdocs github repo](https://github.com/fmatter/pylingdocs/). Here
is some **bold** and *italic* and ***bold italic*** text.

1.  here
2.  is
3.  a
4.  numbered
5.  list

and of course here is

- one
- with
- bullet points[^1]

A quote:

> Locating an individual language on a given point of the
> ergativity-nominativity axis and the diachronic interpretation of this
> axis seem to be conceptually different concerns, even if we were to
> assume that there are principies favouring one direction over the
> other. ([Álvarez 1997](#source-alvarez1998split): 71)

# Pylingdocs markdown

Apart from database references, discussed in [6](#sec:sources), there
are a number of `pylingdocs`-specific commands, all patterning like
links:

- cross-references: [2](#common-markdown) or [1](#sec:intro), see
  corresponding `label` commands
- example references:
  - single \[ex:ekiri-13\]
  - subexample \[ex:ekiri-10\]
  - range: \[ex:ekiri-13–ekiri-11\]
  - or bare: \[ex:tri-1\]
- glosses: ACC
- todos: \[todo: we need to talk about this\]
- tables (with automatically generated table labels like [Table
  3.1](#tab:consonants)):

|           | bilabial | alveolar | palatal | velar | glottal |
|:----------|:---------|:---------|:--------|:------|:--------|
| occlusive | /p /     | /t /     | /ch/    | /k/   |         |
| nasal     | /m /     | /n /     |         |       |         |
| fricative |          | /s /     |         |       | /j/     |
| liquid    |          | /r /     |         |       |         |
| glide     | /w /     |          | /y/     |       |         |

- figures (with automatically generated table labels like [Figure
  3.1](#fig:cognates)):

(Figure 3.1: figures/cognates.jpg)

# Other linguistic data

## Native CLDF components

- forms: Tiriyó pakoro se wae ‘I want a house’ ([Meira
  1999](#source-triomeira1999): 417)
- languages: Hixkaryána
- cognate sets:

None

## Non-native components

Tiriyó *-e* ‘SUP’ ([Meira 1999](#source-triomeira1999): 327) is a
variant of Tiriyó *-(s)e* ([Meira 1999](#source-triomeira1999): 327).
Neither occur on Tiriyó *mahto* ‘fire’ ([Meira
1999](#source-triomeira1999): 314), because it is a noun. They are
related to Apalaí *-se* ([Koehn and Koehn
1986](#source-koehn1986apalai): 77) and Wayana *-(h)e* ([Tavares
2005](#source-wayanatavares2005): 236). This is thus a cognate set
shared by Apalaí, Tiriyó, and Wayana.

- If Tiriyó *kure* ‘good / pretty / well’ ([Meira
  1999](#source-triomeira1999): 345) has too long a translation, try
  Tiriyó *kure* ‘good’ ([Meira 1999](#source-triomeira1999): 345).

- This dataset contains the Ikpeng text The old man.

# Interlinear examples

1)  (ekiri-13)  
    nen        tan   nen        ɨ-wɨ-n  
    INAN.PROX  here  INAN.PROX  1POSS-machete-PERT  
    ‘“My machete is here.”’

2)  

<!-- -->

1)  Ikpeng (ekiri-9)  
    otumunto  mun        eto     ɨ-wɨ-n              otumunto  
    where     INAN.DIST  UNCERT  1POSS-machete-PERT  where  
    ‘“Where might my machete be, where?”’

2)  Ikpeng (ekiri-10)  
    nen-to         nen-to         j-eŋ-lɨ      ɨ-wɨ-n  
    INAN.PROX-LOC  INAN.PROX-LOC  1\>3-put-HOD  1POSS-machete-PERT  
    ‘“Here, here I put my machete.”’

<!-- -->

3)  (tri-1)  
    pai    i-wae    t-ee-se        wïraapa  
    tapir  3-super  NPST-COP-NPST  bow  
    ‘The bow was stronger than the tapir.’

4)  (tri-1)  
    pai    i-wae    t-ee-se        wïraapa  
    tapir  3-super  NPST-COP-NPST  bow  
    ‘The bow was stronger than the tapir.’

5)  (tri-1)  
    pai    i-wae    t-ee-se        wïraapa  
    tapir  3-super  NPST-COP-NPST  bow  
    ‘The bow was stronger than the tapir.’

6)  (tri-1)  
    pai    i-wae    t-ee-se        wïraapa  
    tapir  3-super  NPST-COP-NPST  bow  
    ‘The bow was stronger than the tapir.’

7)  (tri-1)  
    pai    i-wae    t-ee-se        wïraapa  
    tapir  3-super  NPST-COP-NPST  bow  
    ‘The bow was stronger than the tapir.’

## Manual examples

Sometimes you want a non-interlinear example, maybe with a form, or a
simple list, or a table.

8)  

eis

9)  

zwöi

# Citing literature

- see [Álvarez 1997](#source-alvarez1998split) or [Álvarez
  1997](#source-alvarez1998split): 133-134
- with parentheses:
  - “Locating an individual language on a given point of the
    ergativity-nominativity axis and the diachronic interpretation of
    this axis seem to be conceptually different concerns” ([Álvarez
    1997](#source-alvarez1998split))
  - “Locating an individual language on a given point of the
    ergativity-nominativity axis and the diachronic interpretation of
    this axis seem to be conceptually different concerns” ([Álvarez
    1997](#source-alvarez1998split): 71)
- multiple citations:
  - [Álvarez 1997](#source-alvarez1998split): 133-134, [Meira
    1999](#source-triomeira1999): 218
  - ([Álvarez 1997](#source-alvarez1998split): 133-134, [Meira
    1999](#source-triomeira1999): 218)

# References

- <a id="source-alvarez1998split"> </a>Álvarez, José. 1997. Split
  Ergativity and Complementary Distribution of NP’s and Pronominal
  Affixes in Pemón (Cariban). Opción 13. 69–94.
- <a id="source-koehn1986apalai"> </a>Koehn, Edward and Koehn,
  Sally. 1986. Apalai. In Derbyshire, Desmond C. and Pullum, Geoffrey K.
  (eds.), Handbook of Amazonian Languages, 33–127. Berlin/New York:
  Mouton de Gruyter.
- <a id="source-triomeira1999"> </a>Meira, Sérgio. 1999. A Grammar of
  Tiriyó. (Doctoral dissertation).
- <a id="source-wayanatavares2005"> </a>Tavares, Petronila da
  Silva. 2005. A grammar of Wayana. UMI. (Doctoral dissertation).

[^1]: And here is a (foot)note. You can use markdown in here: see
    [4](#sec:data) for details about Apalaí *-se* ‘SUP’ ([Koehn and
    Koehn 1986](#source-koehn1986apalai): 77).