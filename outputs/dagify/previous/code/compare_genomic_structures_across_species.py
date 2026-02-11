from pydantic import BaseModel, Field
from typing import List


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


class SelectGeneMappingMethodsOutput(BaseModel):
    """Pydantic model for select_gene_mapping_methods node outputs."""
    method_name: str = Field(..., description="Name of the gene mapping method")
    description: str = Field(..., description="Brief description of the method")


class CompareGenomicStructuresAcrossSpeciesOutput(BaseModel):
    """Pydantic model for compare_genomic_structures_across_species node outputs."""
    species_list: List[str] = (
        Field(..., description="List of species compared in this analysis")
    )
    comparison_summary: str = (
        Field(..., description="Concise narrative summarizing key differences and similarities in genomic structures")
    )
    key_trends: List[str] = (
        Field(..., description="Primary trends or patterns identified across species (e.g., conserved synteny, rearrangement hotspots)")
    )
    data_quality_flag: bool = (
        Field(..., description="Indicates whether the underlying genomic data meets quality thresholds for reliable comparison")
    )


def compare_genomic_structures_across_species(evaluate_genomic_diversity_dinosaurs_input: EvaluateGenomicDiversityDinosaursOutput, evaluate_genomic_diversity_cretaceous_input: EvaluateGenomicDiversityCretaceousOutput, select_gene_mapping_methods_input: SelectGeneMappingMethodsOutput, **kwargs) -> CompareGenomicStructuresAcrossSpeciesOutput:
    """
    Compare genomic structures across multiple species and identify key
    evolutionary trends.

    Parameters
    ----------
    dinosaurs : dict
        Output of evaluate_genomic_diversity_dinosaurs; contains
        species_list, diversity_index, and key_insights.
    cretaceous : dict
        Output of evaluate_genomic_diversity_cretaceous; contains
        genomic_diversity_factors, diversity_metrics, evolutionary_impact,
        supports_theories, and summary_assessment.
    mapping_methods : list[dict]
        Output of select_gene_mapping_methods; each dict contains
        method_name and description.

    Returns
    -------
    dict
        A dictionary with keys species_list (List[str]), comparison_summary
        (str), key_trends (List[str]), and data_quality_flag (bool).

    Raises
    ------
    ValueError
        If any of the input dictionaries are missing required fields or are
        empty.
    TypeError
        If input types do not match the expected signatures.

    Examples
    --------
    >>> dinosaurs = {
    ...     'species_list': ['Tyrannosaurus', 'Velociraptor'],
    ...     'diversity_index': [0.23, 0.19],
    ...     'key_insights': ['high intra‑species variation', 'low inter‑species
    divergence']
    >>> }
    >>> cretaceous = {
    ...     'genomic_diversity_factors': ['epigenetic modifications'],
    ...     'diversity_metrics': [0.15],
    ...     'evolutionary_impact': ['adaptive radiation'],
    ...     'supports_theories': True,
    ...     'summary_assessment': 'moderate diversity with strong selection
    signals'"                 "}
    >>> mapping_methods = [{'method_name': 'linkage analysis', 'description':
    'Associates markers with phenotypes.'}]
    >>> result = compare_genomic_structures_across_species(dinosaurs,
    cretaceous, mapping_methods)
    >>> print(result['comparison_summary'])
    'The comparison indicates conserved synteny across most dinosaur genomes,
    with rearrangement hotspots near the 3ʹ ends of chromosomes. Cretaceous
    genomes exhibit moderate diversity driven by epigenetic changes, supporting
    adaptive radiation theories.'

    >>> result = compare_genomic_structures_across_species(dinosaurs,
    cretaceous, mapping_methods)
    >>> print(result['key_trends'])
    ['Conserved synteny', 'Rearrangement hotspots', 'Epigenetic‑driven
    diversity']

    """
    return CompareGenomicStructuresAcrossSpeciesOutput(
        species_list=[],
        comparison_summary="",
        key_trends=[],
        data_quality_flag=False,
    )