# select_gene_mapping_methods PRD

## Description
Select and briefly describe commonly used gene mapping methods.


## Conceptual Info

Provides a concise catalog of established gene mapping techniques, enabling downstream analysis nodes to reference the methods employed and understand their basic principles.

## Docstring

### Summary
Return a list of common gene mapping methods and a short description for each.

### Parameters

- **self** (Any): Instance of the node; not used in the function.

### Returns

Dict[str, List[str]]: A dictionary with two keys: 'method_names' containing the names of the methods, and 'method_descriptions' containing concise explanations.

### Raises

- ValueError: If an internal error occurs while compiling the method list.

### Examples

```python
>>> output = select_gene_mapping_methods()
>>> print(output['method_names'])
['Linkage Analysis', 'Physical Mapping', 'Genetic Linkage', 'Positional Cloning', 'Genome-Wide Association Study']
```

```python
>>> output = select_gene_mapping_methods()
>>> print(output['method_descriptions'][0])
'Linkage Analysis: Determines relative positions of genes on a chromosome by studying inheritance patterns in families or pedigrees.'
```
