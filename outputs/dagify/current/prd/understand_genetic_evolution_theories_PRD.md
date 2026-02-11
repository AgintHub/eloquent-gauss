# understand_genetic_evolution_theories PRD

## Description
Explain the fundamental principles of genetic evolution by enumerating and summarizing core concepts.


## Conceptual Info

This node provides a concise yet comprehensive overview of the foundational concepts that drive genetic evolution. The output is structured as paired lists of concept names and their short descriptions, enabling downstream nodes to incorporate these principles into analyses of genomic diversity and gene‑mapping trends.

## Docstring

### Summary
Generate a list of core genetic evolution concepts and brief explanations for each.

### Parameters

- **prompt** (str): A prompt requesting key genetic evolution concepts. The function interprets this prompt and produces a structured list of concepts.

### Returns

Dict[str, List[str]]: A dictionary with two keys: 'concept_names' (a list of concept titles) and 'concept_descriptions' (a list of one‑sentence descriptions corresponding to each name).

### Raises

- ValueError: If the prompt is empty or not a string.

### Examples

```python
>>> output = understand_genetic_evolution_theories(prompt='List key concepts of genetic evolution')
>>> print(output['concept_names'])
>>> print(output['concept_descriptions'])
['Natural Selection', 'Genetic Drift', 'Gene Flow', 'Speciation']
['Mechanism by which advantageous traits become more common in a population over successive generations.', 'Random changes in allele frequencies that can alter genetic variation.', 'Movement of alleles between populations through migration.', 'The process by which new species arise through divergence.']
```

```python
>>> output = understand_genetic_evolution_theories(prompt='')
>>> print(output)
ValueError: Prompt must be a non-empty string.
```
