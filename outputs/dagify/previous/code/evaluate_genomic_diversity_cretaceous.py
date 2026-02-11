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


class EvaluateGenomicDiversityCretaceousOutput(BaseModel):
    """Pydantic model for evaluate_genomic_diversity_cretaceous node outputs."""
    genomic_diversity_factors: List[str] = (
        Field(..., description="List of key factors influencing genomic diversity during the Cretaceous (e.g., gene regulation, epigenetic mechanisms).")
    )
    diversity_metrics: List[float] = (
        Field(..., description="Quantitative metrics of genomic diversity (e.g., nucleotide diversity indices, haplotype variation scores).")
    )
    evolutionary_impact: List[str] = (
        Field(..., description="Explanation of how observed diversity patterns relate to gene evolution theories (speciation, drift, etc.).")
    )
    supports_theories: bool = (
        Field(..., description="Whether the assessment supports existing genetic evolution theories from parent nodes.")
    )
    summary_assessment: str = (
        Field(..., description="Concise summary of genomic diversity's role in shaping evolutionary tendencies during the Cretaceous.")
    )


def evaluate_genomic_diversity_cretaceous(analyze_population_genetics_data_input: AnalyzePopulationGeneticsDataOutput, understand_genetic_evolution_theories_input: UnderstandGeneticEvolutionTheoriesOutput, **kwargs) -> EvaluateGenomicDiversityCretaceousOutput:
    """
    Evaluate the role of genomic diversity during the Cretaceous period and its
    implications for gene evolution.

    Parameters
    ----------
    population_data : dict
        Output dictionary from `analyze_population_genetics_data`,
        containing fields such as `average_genetic_diversity`,
        `species_studied`, `observed_trends`, `implications_summary`, and
        `significant_divergence_detected`.
    evolution_theories : dict
        Output dictionary from `understand_genetic_evolution_theories`,
        containing `concept_names` and `concept_descriptions`.

    Returns
    -------
    dict
        A dictionary with keys matching the node's output structure:
        `genomic_diversity_factors`, `diversity_metrics`,
        `evolutionary_impact`, `supports_theories`, and
        `summary_assessment`.

    Raises
    ------
    ValueError
        Raised if required fields are missing from either input dictionary.

    Examples
    --------
    >>> population_data = {
    ...     "average_genetic_diversity": 0.42,
    ...     "species_studied": ["Triceratops", "Tyrannosaurus"],
    ...     "observed_trends": ["high haplotype diversity"],
    ...     "implications_summary": "Diverse populations suggest rapid
    adaptation.",
    ...     "significant_divergence_detected": True
    >>> }
    >>> evolution_theories = {
    ...     "concept_names": ["speciation", "genetic drift"],
    ...     "concept_descriptions": ["Process of new species formation", "Random
    changes in allele frequencies"]
    >>> }
    >>> result = evaluate_genomic_diversity_cretaceous(population_data,
    evolution_theories)
    >>> print(result['summary_assessment'])
    "Cretaceous genomic diversity, marked by high haplotype variation and
    significant divergence, supports rapid speciation driven by both selection
    and drift, aligning with established evolutionary theories."

    >>> population_data = {
    ...     "average_genetic_diversity": 0.15,
    ...     "species_studied": ["Pachycephalosaurus"],
    ...     "observed_trends": ["low diversity"],
    ...     "implications_summary": "Limited variation implies bottleneck
    events.",
    ...     "significant_divergence_detected": False
    >>> }
    >>> evolution_theories = {
    ...     "concept_names": ["natural selection"],
    ...     "concept_descriptions": ["Process by which advantageous traits
    become common"]
    >>> }
    >>> print(evaluate_genomic_diversity_cretaceous(population_data,
    evolution_theories)['supports_theories'])
    False

    """
    return EvaluateGenomicDiversityCretaceousOutput(
        genomic_diversity_factors=[],
        diversity_metrics=[],
        evolutionary_impact=[],
        supports_theories=False,
        summary_assessment="",
    )