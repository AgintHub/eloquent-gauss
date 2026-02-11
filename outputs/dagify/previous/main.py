import os
import asyncio
import functools
import inspect
import json
import sys
from typing import Dict, Any, List, Callable, Coroutine, Union, Optional

from code.analyze_population_genetics_data import analyze_population_genetics_data
from code.compare_genomic_structures_across_species import compare_genomic_structures_across_species
from code.draw_conclusions_on_gene_mapping_trends import draw_conclusions_on_gene_mapping_trends
from code.evaluate_genomic_diversity_cretaceous import evaluate_genomic_diversity_cretaceous
from code.evaluate_genomic_diversity_dinosaurs import evaluate_genomic_diversity_dinosaurs
from code.identify_key_factors_affecting_gene_evolution import identify_key_factors_affecting_gene_evolution
from code.select_gene_mapping_methods import select_gene_mapping_methods
from code.understand_genetic_evolution_theories import understand_genetic_evolution_theories

# Get async mode from environment variable or default to False
ASYNC_MODE = os.environ.get('ASYNC_MODE', '').lower() in ('true', '1', 'yes', 'y')

def make_async(func):
    """Convert a synchronous function to an asynchronous function.

    If the function is already asynchronous, return it unchanged.
    If the function is synchronous, wrap it in an async function.
    """
    # If it's already a coroutine function, return it as is
    if inspect.iscoroutinefunction(func):
        return func

    # Otherwise, wrap it as an async function
    @functools.wraps(func)
    async def async_wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return async_wrapper

analyze_population_genetics_data_async = make_async(analyze_population_genetics_data)
compare_genomic_structures_across_species_async = make_async(compare_genomic_structures_across_species)
draw_conclusions_on_gene_mapping_trends_async = make_async(draw_conclusions_on_gene_mapping_trends)
evaluate_genomic_diversity_cretaceous_async = make_async(evaluate_genomic_diversity_cretaceous)
evaluate_genomic_diversity_dinosaurs_async = make_async(evaluate_genomic_diversity_dinosaurs)
identify_key_factors_affecting_gene_evolution_async = make_async(identify_key_factors_affecting_gene_evolution)
select_gene_mapping_methods_async = make_async(select_gene_mapping_methods)
understand_genetic_evolution_theories_async = make_async(understand_genetic_evolution_theories)

async def run_workflow(user_input: str) -> Dict[str, Any]:
    """Execute the workflow by running each level in the topological sort.

    Args:
        user_input: The input string for the workflow

    Returns:
        Dict containing all results keyed by node name
    """
    # Store results for each node
    results = {}

    # Level 0: select_gene_mapping_methods, understand_genetic_evolution_theories
    async def run_select_gene_mapping_methods():
        # Call the async version of select_gene_mapping_methods with results from dependencies
        return await select_gene_mapping_methods_async(user_input)

    async def run_understand_genetic_evolution_theories():
        # Call the async version of understand_genetic_evolution_theories with results from dependencies
        return await understand_genetic_evolution_theories_async(user_input)

    # Run level 0 nodes in parallel
    level_0_results = await asyncio.gather(run_select_gene_mapping_methods(), run_understand_genetic_evolution_theories())
    results['select_gene_mapping_methods'] = level_0_results[0]
    results['understand_genetic_evolution_theories'] = level_0_results[1]

    # Level 1: identify_key_factors_affecting_gene_evolution, analyze_population_genetics_data
    async def run_identify_key_factors_affecting_gene_evolution():
        # Call the async version of identify_key_factors_affecting_gene_evolution with results from dependencies
        return await identify_key_factors_affecting_gene_evolution_async(results['select_gene_mapping_methods'], results['understand_genetic_evolution_theories'])

    async def run_analyze_population_genetics_data():
        # Call the async version of analyze_population_genetics_data with results from dependencies
        return await analyze_population_genetics_data_async(results['select_gene_mapping_methods'])

    # Run level 1 nodes in parallel
    level_1_results = await asyncio.gather(run_identify_key_factors_affecting_gene_evolution(), run_analyze_population_genetics_data())
    results['identify_key_factors_affecting_gene_evolution'] = level_1_results[0]
    results['analyze_population_genetics_data'] = level_1_results[1]

    # Level 2: evaluate_genomic_diversity_dinosaurs, evaluate_genomic_diversity_cretaceous
    async def run_evaluate_genomic_diversity_dinosaurs():
        # Call the async version of evaluate_genomic_diversity_dinosaurs with results from dependencies
        return await evaluate_genomic_diversity_dinosaurs_async(results['analyze_population_genetics_data'], results['understand_genetic_evolution_theories'])

    async def run_evaluate_genomic_diversity_cretaceous():
        # Call the async version of evaluate_genomic_diversity_cretaceous with results from dependencies
        return await evaluate_genomic_diversity_cretaceous_async(results['analyze_population_genetics_data'], results['understand_genetic_evolution_theories'])

    # Run level 2 nodes in parallel
    level_2_results = await asyncio.gather(run_evaluate_genomic_diversity_dinosaurs(), run_evaluate_genomic_diversity_cretaceous())
    results['evaluate_genomic_diversity_dinosaurs'] = level_2_results[0]
    results['evaluate_genomic_diversity_cretaceous'] = level_2_results[1]

    # Level 3: compare_genomic_structures_across_species
    async def run_compare_genomic_structures_across_species():
        # Call the async version of compare_genomic_structures_across_species with results from dependencies
        return await compare_genomic_structures_across_species_async(results['evaluate_genomic_diversity_dinosaurs'], results['evaluate_genomic_diversity_cretaceous'], results['select_gene_mapping_methods'])

    # Run level 3 nodes in parallel
    results['compare_genomic_structures_across_species'] = await run_compare_genomic_structures_across_species()

    # Level 4: draw_conclusions_on_gene_mapping_trends
    async def run_draw_conclusions_on_gene_mapping_trends():
        # Call the async version of draw_conclusions_on_gene_mapping_trends with results from dependencies
        return await draw_conclusions_on_gene_mapping_trends_async(results['compare_genomic_structures_across_species'])

    # Run level 4 nodes in parallel
    results['draw_conclusions_on_gene_mapping_trends'] = await run_draw_conclusions_on_gene_mapping_trends()

    # Return all results
    return results

def run_workflow_sync(user_input: str) -> Dict[str, Any]:
    """Synchronous wrapper around the async workflow execution."""
    return asyncio.run(run_workflow(user_input))

def main():
    """Main entry point.

    Handles arguments in the following priority:
    1. Command-line argument (sys.argv[1])
    2. If no argument, uses empty string as input but displays a warning.
    """
    # Get user input from command line or use empty string
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
    else:
        # No input provided - display help message but continue with empty string
        print('Warning: No input provided. Using empty string as input.')
        print('For better results, provide an input argument:')
        print(f'  python {os.path.basename(__file__)} "your input text here"')
        print('Or use a file as input:')
        print(f'  python {os.path.basename(__file__)} "$(cat input.txt)"')
        user_input = ""

    print(f'Running workflow with input: {user_input}')

    # Run the workflow
    results = run_workflow_sync(user_input)

    # Print results
    try:
        # Convert results to JSON
        json_results = json.dumps(results, indent=2, default=str)
        print(json_results)
    except (TypeError, ValueError) as e:
        print(f'Results could not be converted to JSON: {e}')
        print(f'Raw results: {results}')

    return results

if __name__ == '__main__':
    main()
