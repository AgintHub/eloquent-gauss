# identify_key_factors_affecting_gene_evolution PRD

## Description
Identify the primary biological processes and demographic forces that drive changes in gene frequencies over time, producing a concise list of key factors.


## Conceptual Info

This node extracts and compiles the fundamental drivers of gene evolution from the literature and conceptual frameworks provided by its parent nodes. It consolidates complex evolutionary mechanisms into a user‑friendly list that can be leveraged by downstream nodes for mapping strategies, hypothesis generation, or educational summaries.

## Docstring

### Summary
Return a list of the primary biological factors that drive gene evolution.

### Parameters

- **input_text** (str): Free‑text input that may contain a mixture of literature excerpts, theory summaries, or user prompts. The function processes this text to identify mentions of evolutionary mechanisms.

### Returns

List[str]: A list of concise, human‑readable factor names (e.g., "mutation", "recombination"). The order of items reflects their relative prominence as indicated by the input.

### Raises

- ValueError: If input_text is an empty string or contains only whitespace.
- RuntimeError: If the function cannot extract any valid factors after applying its parsing heuristics.

### Examples

```python
>>> identify_key_factors_affecting_gene_evolution('Recombination, mutation, and genetic drift are central to evolution.')
['recombination', 'mutation', 'genetic drift']
```

```python
>>> identify_key_factors_affecting_gene_evolution('Population structure, natural selection, and gene flow shape genomes.')
['population structure', 'natural selection', 'gene flow']
```
