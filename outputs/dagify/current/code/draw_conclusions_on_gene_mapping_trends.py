from pydantic import BaseModel, Field
from typing import List


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


class DrawConclusionsOnGeneMappingTrendsOutput(BaseModel):
    """Pydantic model for draw_conclusions_on_gene_mapping_trends node outputs."""
    conclusion_text: str = (
        Field(..., description="A concise textual summary of the main conclusions drawn from the analysis.")
    )
    key_trends: List[str] = (
        Field(..., description="A list of the most significant evolutionary trends identified in gene mapping across species.")
    )
    implications: List[str] = (
        Field(..., description="A list of implications these trends have for our broader understanding of genetic evolution.")
    )


def draw_conclusions_on_gene_mapping_trends(compare_genomic_structures_across_species_input: CompareGenomicStructuresAcrossSpeciesOutput, **kwargs) -> DrawConclusionsOnGeneMappingTrendsOutput:
    """
    Generate a concise conclusion and implications from comparative genomic
    structure analyses.

    Parameters
    ----------
    species_list : List[str]
        List of species that were compared in the genomic structure
        analysis.
    comparison_summary : str
        Narrative summary produced by the comparison node detailing
        differences and similarities in genomic architectures.
    key_trends : List[str]
        Primary evolutionary trends identified during the comparison (e.g.,
        conserved synteny, chromosomal rearrangement hotspots).
    data_quality_flag : bool
        Flag indicating whether the underlying genomic data met quality
        thresholds for reliable comparison.

    Returns
    -------
    dict
        Dictionary containing three keys: "conclusion_text", "key_trends",
        and "implications". The types correspond to the node's output
        structure.

    Raises
    ------
    ValueError
        If data_quality_flag is False, indicating unreliable input data.
    TypeError
        If any of the input parameters do not match the expected types.

    Examples
    --------
    >>> species_list = ["Anas platyrhynchos", "Gallus gallus", "Taeniopygia
    guttata"],
    >>> comparison_summary = "Across the three avian genomes, synteny is largely
    conserved, yet a notable translocation is present on chromosome 2 in the
    duck.",
    >>> key_trends = ["Conserved synteny", "Chromosomal translocation in duck"],
    >>> data_quality_flag = True
    >>> result = draw_conclusions_on_gene_mapping_trends(species_list,
    comparison_summary, key_trends, data_quality_flag)
    >>> print(result["conclusion_text"])
    >>> print(result["key_trends"])
    >>> print(result["implications"])
    "Conservation of synteny across the examined avian species suggests strong
    selective pressure to maintain genomic architecture, while the duck-specific
    translocation indicates lineage‑specific rearrangement events. These
    patterns imply that genome stability is a key evolutionary strategy, yet
    structural variation remains a mechanism for diversification.
    
    ["Conserved synteny", "Chromosomal translocation in duck"]
    
    ["Genome stability is a common selective pressure across avian lineages.",
    "Lineage‑specific rearrangements can drive rapid adaptation."]

    >>> species_list = ["Homo sapiens", "Pan troglodytes", "Macaca mulatta"],
    >>> comparison_summary = "Human and chimpanzee genomes share extensive
    synteny, whereas macaque shows several inversions.",
    >>> key_trends = ["High synteny in primates", "Inversion hotspots in
    macaque"],
    >>> data_quality_flag = False
    >>> draw_conclusions_on_gene_mapping_trends(species_list,
    comparison_summary, key_trends, data_quality_flag)
    ValueError: Data quality insufficient for reliable conclusion generation.

    """
    return DrawConclusionsOnGeneMappingTrendsOutput(
        conclusion_text="",
        key_trends=[],
        implications=[],
    )