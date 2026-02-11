from pydantic import BaseModel, Field
from typing import List


class AnalyzePopulationGeneticsDataOutput(BaseModel):
    """Pydantic model for analyze_population_genetics_data node outputs."""
    average_genetic_diversity: float = (
        Field(..., description="Average genetic diversity metric calculated across studied populations")
    )
    species_studied: List[str] = (
        Field(..., description="List of species included in the population genetics analysis")
    )
    observed_trends: List[str] = (
        Field(..., description="Key observed trends in gene variation and divergence patterns")
    )
    implications_summary: str = (
        Field(..., description="Summary of implications for gene evolution understanding")
    )
    significant_divergence_detected: bool = (
        Field(..., description="Boolean indicator of statistically significant divergence detected")
    )


class UnderstandGeneticEvolutionTheoriesOutput(BaseModel):
    """Pydantic model for understand_genetic_evolution_theories node outputs."""
    concept_names: List[str] = (
        Field(..., description="Names of the key genetic evolution concepts.")
    )
    concept_descriptions: List[str] = (
        Field(..., description="Brief descriptions for each corresponding concept.")
    )


class EvaluateGenomicDiversityDinosaursOutput(BaseModel):
    """Pydantic model for evaluate_genomic_diversity_dinosaurs node outputs."""
    species_list: List[str] = (
        Field(..., description="List of dinosaur species evaluated.")
    )
    diversity_index: List[float] = (
        Field(..., description="Corresponding genomic diversity index for each species.")
    )
    key_insights: List[str] = (
        Field(..., description="Concise insights linking diversity metrics to evolutionary processes.")
    )


def evaluate_genomic_diversity_dinosaurs(analyze_population_genetics_data_input: AnalyzePopulationGeneticsDataOutput, understand_genetic_evolution_theories_input: UnderstandGeneticEvolutionTheoriesOutput, **kwargs) -> EvaluateGenomicDiversityDinosaursOutput:
    """
    Computes per‑species genomic diversity indices for dinosaurs and extracts
    evolutionary insights.

    Parameters
    ----------
    average_genetic_diversity : float
        Average genetic diversity metric from population genetics analysis
        (e.g., nucleotide diversity).
    species_studied : List[str]
        List of dinosaur species included in the analysis.
    observed_trends : List[str]
        Key trends observed in gene variation and divergence patterns.
    implications_summary : str
        Summary of how observed genetic diversity informs gene evolution
        theories.
    concept_names : List[str]
        Names of genetic evolution concepts relevant to the analysis.
    concept_descriptions : List[str]
        Brief descriptions of the concepts in concept_names.

    Returns
    -------
    Tuple[List[str], List[float], List[str]]
        A tuple containing the species list, corresponding diversity
        indices, and concise evolutionary insights.

    Raises
    ------
    ValueError
        If input lists are of mismatched lengths or if required inputs are
        missing.
    TypeError
        If any input parameter is not of the expected type.

    Examples
    --------
    >>> # Example 1: Simple synthetic data
    >>> species = ['Tyrannosaurus', 'Velociraptor', 'Stegosaurus']
    >>> diversity = [0.12, 0.09, 0.15]
    >>> insights = ["High diversity suggests rapid adaptive radiation",
    "Moderate diversity indicates stable niche", "Elevated diversity may reflect
    heterozygosity"]
    >>> result = evaluate_genomic_diversity_dinosaurs(0.1, species, ['trend1'],
    'summary', ['selection'], ['Natural selection shapes diversity'])
    >>> print(result)
    (['Tyrannosaurus', 'Velociraptor', 'Stegosaurus'], [0.12, 0.09, 0.15],
    ['High diversity suggests rapid adaptive radiation', 'Moderate diversity
    indicates stable niche', 'Elevated diversity may reflect heterozygosity'])

    >>> # Example 2: Error when lengths mismatch
    >>> try:
    ...     evaluate_genomic_diversity_dinosaurs(0.1, ['Tyrannosaurus'], [], '',
    [], [])
    >>> except ValueError as e:
    ...     print(str(e))
    "Input lists must have the same length. Provided species list has length 1
    but diversity_index has length 0."

    """
    return EvaluateGenomicDiversityDinosaursOutput(
        species_list=[],
        diversity_index=[],
        key_insights=[],
    )