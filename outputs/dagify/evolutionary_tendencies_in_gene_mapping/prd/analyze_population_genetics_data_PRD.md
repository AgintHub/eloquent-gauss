# analyze_population_genetics_data PRD

## Description
Analyze data from existing population genetics studies on gene variation and divergence.


## Conceptual Info

This node analyzes population genetics data to understand gene variation and divergence across species.

## Docstring

### Summary
Analyzes existing population genetics data to summarize gene variation patterns and genetic divergence across species.

### Parameters

- **gene_mapping_methods** (List[str]): List of gene mapping methods selected and described in the parent node 'select_gene_mapping_methods'.

### Returns

{species_list: List[str], variation_summary: str, divergence_metrics: str}: A dictionary containing a list of species analyzed, a summary of gene variation patterns, and metrics of genetic divergence.

### Raises

- ValueError: If the input data from parent nodes is incomplete or improperly formatted.

### Examples

```python
>>> analyze_population_genetics_data(gene_mapping_methods=['linkage_analysis', 'physical_mapping'])
{'species_list': ['Homo sapiens', 'Mus musculus'], 'variation_summary': 'High genetic variation in coding regions', 'divergence_metrics': 'Average nucleotide divergence of 0.05'}
```
