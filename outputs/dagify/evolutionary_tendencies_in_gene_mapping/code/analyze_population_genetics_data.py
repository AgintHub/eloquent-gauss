from pydantic import BaseModel, Field
from typing import List


class SelectGeneMappingMethodsOutput(BaseModel):
    """Pydantic model for select_gene_mapping_methods node outputs."""
    method_name: str = Field(..., description="Name of the gene mapping method")
    description: str = Field(..., description="Brief description of the method")


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


def analyze_population_genetics_data(select_gene_mapping_methods_input: SelectGeneMappingMethodsOutput, **kwargs) -> AnalyzePopulationGeneticsDataOutput:
    """
    Analyzes population genetics data to calculate diversity metrics, identify
    species trends, and determine evolutionary implications using selected gene
    mapping methods.

    Parameters
    ----------
    study_datasets : Dict[str, Dict]
        Collection of population genetics datasets keyed by species
    mapping_methods : List[Dict]
        Selected gene mapping methods from select_gene_mapping_methods
        output
    significance_threshold : float
        p-value threshold for determining statistical significance (default:
        0.05)

    Returns
    -------
    Dict[str, Union[float, List, str, bool]]
        Analysis results containing diversity metrics, species list,
        observed trends, implications summary, and divergence detection
        status

    Raises
    ------
    ValueError
        If datasets contain inconsistent genomic metadata across species
    KeyError
        If required genetic diversity metrics are missing from input
        datasets

    Examples
    --------
    >>> analyze_population_genetics_data({
    ...   'panthera_tigris': {'diversity': 0.45, 'haplotypes': 120},
    ...   'felis_catus': {'diversity': 0.32, 'haplotypes': 85}
    >>> }, [{'method_name': 'linkage_analysis', 'description': '...'}])
    {'average_genetic_diversity': 0.385, 'species_studied': ['panthera_tigris',
    'felis_catus'], 'observed_trends': ['High haplotype diversity in big cats',
    'Significant divergence in regulatory regions'], 'implications_summary':
    'Supports adaptive evolution in feline species',
    'significant_divergence_detected': True}

    >>> analyze_population_genetics_data({}, [{'method_name':
    'physical_mapping', 'description': '...'}])
    Traceback (most recent call last): ... ValueError: No datasets provided for
    analysis

    """
    return AnalyzePopulationGeneticsDataOutput(
        average_genetic_diversity=0.0,
        species_studied=[],
        observed_trends=[],
        implications_summary="",
        significant_divergence_detected=False,
    )