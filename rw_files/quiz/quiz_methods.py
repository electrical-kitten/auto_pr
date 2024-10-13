from pathlib import Path


def get_file_path(path_string):
    gen_path = Path.cwd() / path_string
    return gen_path
