import os

def validate_output_path(path):
    if not path:
        return None
    if not os.path.exists(path):
        os.makedirs(path)
    return path
