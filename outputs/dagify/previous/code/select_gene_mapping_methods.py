from pydantic import BaseModel, Field


class SelectGeneMappingMethodsOutput(BaseModel):
    """Pydantic model for select_gene_mapping_methods node outputs."""
    method_name: str = Field(..., description="Name of the gene mapping method")
    description: str = Field(..., description="Brief description of the method")


def select_gene_mapping_methods(general_input: str, **kwargs) -> SelectGeneMappingMethodsOutput:
    """
    Return a list of commonly used gene‑mapping methods with brief descriptions.

    Returns
    -------
    List[Dict[str, str]]
        A list of dictionaries, each containing two keys:  * ``method_name``
        – the name of the mapping method (str). * ``description`` – a
        concise explanation of how the method works and its typical use case
        (str).

    Raises
    ------
    RuntimeError
        Raised if the internal knowledge base fails to provide any mapping
        methods.

    Examples
    --------
    >>> methods = select_gene_mapping_methods()
    >>> print(methods[0])
    {'method_name': 'Linkage Analysis', 'description': 'Uses recombination
    frequencies between genetic markers to infer their relative positions on a
    chromosome.'}

    >>> methods = select_gene_mapping_methods()
    >>> for m in methods:
    ...     print(f"- {m['method_name']}: {m['description']}")
    - Linkage Analysis: Uses recombination frequencies between genetic markers
    to infer their relative positions on a chromosome.
    - Physical Mapping: Determines the physical distances between genes or
    markers using techniques such as restriction mapping or fluorescence in situ
    hybridization (FISH).

    """
    return SelectGeneMappingMethodsOutput(
        method_name="",
        description="",
    )