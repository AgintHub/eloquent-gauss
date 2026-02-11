# select_gene_mapping_methods PRD

## Description
Generate a concise catalog of commonly used gene mapping techniques, providing each method’s name and a brief description of its principle and typical application.


## Conceptual Info

This node collates a short list of well‑established gene‑mapping approaches, furnishing the name and a succinct explanatory note for each. The output can be used as reference material for downstream analysis nodes that require an understanding of the mapping techniques applied to the data.

## Docstring

### Summary
Return a list of commonly used gene‑mapping methods with brief descriptions.

### Returns

List[Dict[str, str]]: A list of dictionaries, each containing two keys:

* ``method_name`` – the name of the mapping method (str).
* ``description`` – a concise explanation of how the method works and its typical use case (str).

### Raises

- RuntimeError: Raised if the internal knowledge base fails to provide any mapping methods.

### Examples

```python
>>> methods = select_gene_mapping_methods()
>>> print(methods[0])
{'method_name': 'Linkage Analysis', 'description': 'Uses recombination frequencies between genetic markers to infer their relative positions on a chromosome.'}
```

```python
>>> methods = select_gene_mapping_methods()
>>> for m in methods:
...     print(f"- {m['method_name']}: {m['description']}")
- Linkage Analysis: Uses recombination frequencies between genetic markers to infer their relative positions on a chromosome.
- Physical Mapping: Determines the physical distances between genes or markers using techniques such as restriction mapping or fluorescence in situ hybridization (FISH).
```
