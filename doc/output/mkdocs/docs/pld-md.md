
# Pylingdocs markdown { #pld-md }

Apart from database references, discussed in <a href='#sec:sources' class='crossref' name='sec:sources' >ref</a>, there are a number of `pylingdocs`-specific commands, all patterning like links:

* cross-references: <a href='#common-markdown' class='crossref' name='common-markdown' >ref</a> or <a href='#sec:intro' class='crossref' name='sec:intro' >ref</a>, see corresponding `label` commands
* example references:
    * single <a class="exref" example_id="ekiri-13" ></a>
    * subexample <a class="exref" example_id="ekiri-10" ></a>
    * range: <a class="exref" example_id="ekiri-13" end="ekiri-11" ></a>
    * or bare: <a class="exref" example_id="ekiri-11" bare></a>
* glosses: <span class='gloss'>acc<span class='tooltiptext gloss-acc'></span></span>
* todos: <span title='we need to talk about this'>❗️</span>
* tables (with automatically generated table labels like <a href='#tab:consonants' class='crossref' name='tab:consonants' >ref</a>):


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

* figures (with automatically generated table labels like <a href='#fig:cognates' class='crossref' name='fig:cognates' >ref</a>):

<figure>
<img src="/figures/cognates.jpg" alt="Cognate identification strategy" />
<figcaption id="fig:cognates" aria-hidden="true">Cognate identification strategy</figcaption>
</figure>
