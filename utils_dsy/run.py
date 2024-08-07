import subprocess
import os

from utils_dsy.map_data import model_name_map
from utils_dsy.map_data import transformers_map


def get_runtime_model_name(model_name):
    """
    Retrieve the runtime model name identifier from model_name_map.

    Args:
    model_name (str): Human-readable model name.

    Returns:
    str: The internal identifier used in the code for the given model name.
    """
    return model_name_map.get(model_name, model_name)


def get_transformers_version(model_name, transformers_map):
    """
    Retrieve the transformers version for a given model name using both exact and flexible matching.

    Parameters:
    model_name (str): The model name to search for.
    transformers_map (dict): The dictionary containing model series and their corresponding transformers versions.

    Returns:
    str: The version of transformers required for the model, or a message if no match is found.
    """
    # Try exact match first
    if model_name in transformers_map:
        return transformers_map[model_name]

    # Create a simplified version of the transformers map for flexible matching inside the function
    # Only remove ' Series' from the keys for flexible matching
    simplified_map = {key.replace(' Series', '').replace(' series', ''): transformers_map[key] for key in transformers_map.keys()}

    # Attempt to find a flexible match
    for key in simplified_map:
        if key.lower() in model_name.lower():
            return simplified_map[key]

    # If no match is found, return an error message
    return 'No transformers version found for the specified model.'


def main():
    cur_file_path = os.path.abspath(__file__)
    # Get Parent directory
    parent_dir = os.path.dirname(cur_file_path)
    work_root = os.path.dirname(parent_dir)
    model_list_path = os.path.join(parent_dir, 'model_list.txt')

    with open(model_list_path, 'r') as file:
        for line in file:
            model_name = line.strip()
            version = get_transformers_version(model_name, transformers_map)
            if version:
                if version == 'latest':
                    conda_env = 'tf_latest'
                else:
                    major_minor = '.'.join(version.split('.')[:2])
                    conda_env = f"tf_{major_minor.replace('.', '')}"
                print(f'Activating conda environment: {conda_env} for model: {model_name}')
                # Ensure the command runs in the specified conda environment
                runtime_model_name = get_runtime_model_name(model_name)
                command = f'conda run -n {conda_env} torchrun --nproc-per-node=4 {work_root}/run.py --data OCRVQA_TESTCORE --model {runtime_model_name} --verbose'
                # Running the command with output and error displayed in the console
                print(f'Running command: {command}')

                process = subprocess.run(command, shell=True)
            else:
                print(f'No version found for {model_name}')

if __name__ == '__main__':
    main()
