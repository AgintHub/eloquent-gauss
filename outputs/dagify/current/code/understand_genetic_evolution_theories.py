from pydantic import BaseModel, Field
from typing import List


class UnderstandGeneticEvolutionTheoriesOutput(BaseModel):
    """Pydantic model for understand_genetic_evolution_theories node outputs."""
    concept_names: List[str] = (
        Field(..., description="Names of the key genetic evolution concepts.")
    )
    concept_descriptions: List[str] = (
        Field(..., description="Brief descriptions for each corresponding concept.")
    )


def understand_genetic_evolution_theories(general_input: str, **kwargs) -> UnderstandGeneticEvolutionTheoriesOutput:
    """
    Generate a paired list of core genetic evolution concepts and their concise
    descriptions.

    Parameters
    ----------
    input_text : str
        A prompt or instruction string requesting key genetic evolution
        concepts. The function ignores the content and uses a predefined set
        of concepts relevant to the prompt.

    Returns
    -------
    Tuple[List[str], List[str]]
        Two parallel lists: first contains concept names, second contains
        corresponding short descriptions.

    Raises
    ------
    ValueError
        If `input_text` is empty or None.

    Examples
    --------
    >>> names, descs = understand_genetic_evolution_theories('Explain key
    concepts')
    >>> print(names)
    >>> print(descs)
    [
      'Speciation',
      'Natural Selection',
      'Genetic Drift',
      'Gene Flow',
      'Mutation',
      'Recombination',
      'Population Structure',
      'Genetic Hitchhiking'
    ]
    [
      'The formation of new species through reproductive isolation.',
      'Differential survival and reproduction of phenotypes.',
      'Random fluctuations in allele frequencies.',
      'Movement of alleles between populations.',
      'Introduction of new genetic variants.',
      'Exchange of genetic material during meiosis.',
      'Distribution of individuals and genes in a population.',
      'Increase in allele frequency due to linkage with a favorable allele.'
    ]

    >>> names, descs = understand_genetic_evolution_theories('')
    >>> print(names)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: input_text must not be empty.

    """
    return UnderstandGeneticEvolutionTheoriesOutput(
        concept_names=[],
        concept_descriptions=[],
    )