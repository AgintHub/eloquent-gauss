# compare_genomic_structures_across_species PRD

## Description
Analyze the genomic structure of various species and draw conclusions on gene mapping trends


## Conceptual Info

The node aggregates genomic architecture metrics from dinosaur and Cretaceous period analyses, applies selected gene‑mapping methods, and produces a species‑level comparative summary highlighting structural conservation, rearrangement hotspots, and data reliability.

## Docstring

### Summary
Compare genomic structures across multiple species and identify key evolutionary trends.

### Parameters

- **dinosaurs** (dict): Output of evaluate_genomic_diversity_dinosaurs; contains species_list, diversity_index, and key_insights.
- **cretaceous** (dict): Output of evaluate_genomic_diversity_cretaceous; contains genomic_diversity_factors, diversity_metrics, evolutionary_impact, supports_theories, and summary_assessment.
- **mapping_methods** (list[dict]): Output of select_gene_mapping_methods; each dict contains method_name and description.

### Returns

dict: A dictionary with keys species_list (List[str]), comparison_summary (str), key_trends (List[str]), and data_quality_flag (bool).

### Raises

- ValueError: If any of the input dictionaries are missing required fields or are empty.
- TypeError: If input types do not match the expected signatures.

### Examples

```python
>>> dinosaurs = {
...     'species_list': ['Tyrannosaurus', 'Velociraptor'],
...     'diversity_index': [0.23, 0.19],
...     'key_insights': ['high intra‑species variation', 'low inter‑species divergence']
>>> }
>>> cretaceous = {
...     'genomic_diversity_factors': ['epigenetic modifications'],
...     'diversity_metrics': [0.15],
...     'evolutionary_impact': ['adaptive radiation'],
...     'supports_theories': True,
...     'summary_assessment': 'moderate diversity with strong selection signals'"
                "}
>>> mapping_methods = [{'method_name': 'linkage analysis', 'description': 'Associates markers with phenotypes.'}]
>>> result = compare_genomic_structures_across_species(dinosaurs, cretaceous, mapping_methods)
>>> print(result['comparison_summary'])
'The comparison indicates conserved synteny across most dinosaur genomes, with rearrangement hotspots near the 3ʹ ends of chromosomes. Cretaceous genomes exhibit moderate diversity driven by epigenetic changes, supporting adaptive radiation theories.'
```

```python
>>> result = compare_genomic_structures_across_species(dinosaurs, cretaceous, mapping_methods)
>>> print(result['key_trends'])
['Conserved synteny', 'Rearrangement hotspots', 'Epigenetic‑driven diversity']
```
