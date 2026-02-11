# compare_genomic_structures_across_species PRD

## Description
Analyze the genomic structure of various species and draw conclusions on gene mapping trends.


## Conceptual Info

This node synthesizes genomic diversity metrics and gene mapping method outputs to produce a high‑level comparative report. It identifies structural differences across genomes, highlights recurrent mapping patterns, and flags species with exceptional divergence, thereby informing downstream evolutionary interpretation.

## Docstring

### Summary
Compare genomic structures across species and summarize gene‑mapping trends.

### Parameters

- **diversity_data** (Dict[str, Any]): Output from `evaluate_genomic_diversity_across_species`, containing species list, diversity scores, key factors, and a conclusion summary.
- **mapping_methods** (Dict[str, Any]): Output from `select_gene_mapping_methods`, listing available gene mapping methods and brief descriptions.

### Returns

Dict[str, Any]: A dictionary containing the species list, a narrative summary of genomic comparisons, key gene‑mapping trends, species with the highest divergence, and the mapping methods employed.

### Raises

- ValueError: If either input dictionary is missing required keys or contains empty lists.
- TypeError: If input types do not match expected structures.

### Examples

```python
>>> diversity_data = {
...     'species_list': ['Human', 'Chimpanzee', 'Mouse'],
...     'diversity_scores': [0.1, 0.12, 0.3],
...     'key_factors': ['gene regulation', 'epigenetics', 'mutation rate'],
...     'conclusion_summary': ['High diversity in Mouse due to rapid mutation']
>>> }
>>> mapping_methods = {
...     'method_names': ['Linkage analysis', 'Physical mapping'],
...     'method_descriptions': [
...         'Analyzes recombination frequencies between markers',
...         'Uses physical distances on chromosomes to map genes']
>>> }
{\n  'species_list': ['Human', 'Chimpanzee', 'Mouse'],\n  'genomic_comparison_summary': 'Human and Chimpanzee share conserved synteny; Mouse shows extensive rearrangements.',\n  'key_gene_mapping_trends': ['Conserved linkage groups between primates', 'Higher breakpoint density in Mouse'],\n  'species_with_highest_divergence': ['Mouse'],\n  'mapping_method_used': ['Linkage analysis', 'Physical mapping']\n}
```

```python
>>> # Handling missing diversity scores
>>> diversity_data = {
...     'species_list': ['Human', 'Mouse'],
...     'diversity_scores': [],
...     'key_factors': ['mutation rate'],
...     'conclusion_summary': []
>>> }
>>> mapping_methods = {
...     'method_names': [],
...     'method_descriptions': []
>>> }
ValueError: Input dictionaries must contain non‑empty lists for species_list, diversity_scores, method_names, and method_descriptions.
```
