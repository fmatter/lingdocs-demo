
# Pylingdocs markdown { #pld-md }

Apart from database references, discussed in [6](site:/sec:sources#sec:sources), there are a number of `pylingdocs`-specific commands, all patterning like links:

* cross-references: [2](site:/common-markdown#common-markdown) or [1](site:/sec:intro#sec:intro), see corresponding `label` commands
* example references:
    * single <a class="exref" example_id="ekiri-13" ></a>
    * subexample <a class="exref" example_id="ekiri-10" ></a>
    * range: <a class="exref" example_id="ekiri-13" end="ekiri-11" ></a>
    * or bare: <a class="exref" example_id="tri-1" bare></a>
* glosses: <span class='gloss'>acc<span class='tooltiptext gloss-acc'></span></span>
* todos: <span title='we need to talk about this'>❕</span>
* tables (with automatically generated table labels like [Table 3.1](site:/pld-md#tab:consonants)):


<table border="1" class="dataframe">
<caption class='table' id ='tab:consonants'>Consonant phonemes of Yawarana</caption><thead>
<tr >
<th>
</th>
<th>
bilabial
</th>
<th>
alveolar
</th>
<th>
palatal
</th>
<th>
velar
</th>
<th>
glottal
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
occlusive
</td>
<td>
/p /
</td>
<td>
/t /
</td>
<td>
/ch/
</td>
<td>
/k/
</td>
<td>
</td>
</tr>
<tr>
<td>
nasal
</td>
<td>
/m /
</td>
<td>
/n /
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
fricative
</td>
<td>
</td>
<td>
/s /
</td>
<td>
</td>
<td>
</td>
<td>
/j/
</td>
</tr>
<tr>
<td>
liquid
</td>
<td>
</td>
<td>
/r /
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
glide
</td>
<td>
/w /
</td>
<td>
</td>
<td>
/y/
</td>
<td>
</td>
<td>
</td>
</tr>
</tbody>
</table>

* figures (with automatically generated table labels like [Figure 3.1](site:/pld-md#fig:cognates)):

<figure>
<img src="/figures/cognates.jpg" alt="Cognate identification strategy" />
<figcaption id="fig:cognates" aria-hidden="true">Cognate identification strategy</figcaption>
</figure>
