var abbrev_dict={'cor': 'coreferential', 'hod': 'hodiernal past', 'cont': 'continuous', 'part': 'particle', 'ideo': 'ideophone', 'iter': 'iterative', 'rem': 'remove past', 'uncert': 'uncertainty', 'inan': 'inanimate', 'aff': 'affirmative', 'npst': 'non-past', 'pert': 'pertensive', 'ill': 'illative', 'sup': 'supine', 'obl': 'oblique', '3': 'third person', '1': 'first person', 'poss': 'possessive', 'dist': 'distal', '2': 'second person', 'loc': 'locative', 'nmlz': 'nominalizer/nominalization', 'prox': 'proximal/proximate', 'voc': 'vocative', 'rel': 'relative', 'aux': 'auxiliary', 'pl': 'plural', 'ins': 'instrumental', 'cop': 'copula', 'acc': 'accusative'}; for (var key in abbrev_dict){
var targets = document.getElementsByClassName('gloss-'+key)
for (var i = 0; i < targets.length; i++) {
    targets[i].innerHTML = abbrev_dict[key];
}
};
