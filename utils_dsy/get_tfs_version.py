from vlmeval.tools import models

def get_model_version(model_name):
    """
    Returns the version of the given model name.

    Args:
    model_name (str): The name of the model to lookup.

    Returns:
    str: The version of the model, or 'Unknown' if the model is not found.
    """
    for version, model_list in models.items():
        if model_name in model_list:
            return version
    return 'Unknown'

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python get_tfs_version.py [model_name] ...")
        sys.exit(1)

    # Handle multiple model names from command line arguments
    for model_name in sys.argv[1:]:
        version = get_model_version(model_name)
        print(f"Model '{model_name}' uses transformers version: {version}")
