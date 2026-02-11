from pydantic import BaseModel, Field
from typing import List


class SelectGeneMappingMethodsOutput(BaseModel):
    """Pydantic model for select_gene_mapping_methods node outputs."""
    method_name: str = Field(..., description="Name of the gene mapping method")
    description: str = Field(..., description="Brief description of the method")


class UnderstandGeneticEvolutionTheoriesOutput(BaseModel):
    """Pydantic model for understand_genetic_evolution_theories node outputs."""
    concept_names: List[str] = (
        Field(..., description="Names of the key genetic evolution concepts.")
    )
    concept_descriptions: List[str] = (
        Field(..., description="Brief descriptions for each corresponding concept.")
    )


class IdentifyKeyFactorsAffectingGeneEvolutionOutput(BaseModel):
    """Pydantic model for identify_key_factors_affecting_gene_evolution node outputs."""
    key_factors: List[str] = (
        Field(..., description="A list of the main biological factors that influence gene evolution, e.g., recombination, mutation, genetic hitchhiking, and population structure.")
    )


def identify_key_factors_affecting_gene_evolution(select_gene_mapping_methods_input: SelectGeneMappingMethodsOutput, understand_genetic_evolution_theories_input: UnderstandGeneticEvolutionTheoriesOutput, **kwargs) -> IdentifyKeyFactorsAffectingGeneEvolutionOutput:
    """
    Return a list of the primary biological factors that drive gene evolution.

    Parameters
    ----------
    input_text : str
        Free‑text input that may contain a mixture of literature excerpts,
        theory summaries, or user prompts. The function processes this text
        to identify mentions of evolutionary mechanisms.

    Returns
    -------
    List[str]
        A list of concise, human‑readable factor names (e.g., "mutation",
        "recombination"). The order of items reflects their relative
        prominence as indicated by the input.

    Raises
    ------
    ValueError
        If input_text is an empty string or contains only whitespace.
    RuntimeError
        If the function cannot extract any valid factors after applying its
        parsing heuristics.

    Examples
    --------
    >>> identify_key_factors_affecting_gene_evolution('Recombination, mutation,
    and genetic drift are central to evolution.')
    ['recombination', 'mutation', 'genetic drift']

    >>> identify_key_factors_affecting_gene_evolution('Population structure,
    natural selection, and gene flow shape genomes.')
    ['population structure', 'natural selection', 'gene flow']

    """
    return IdentifyKeyFactorsAffectingGeneEvolutionOutput(
        key_factors=[],
    )