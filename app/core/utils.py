from pathlib import Path


def resolve_path_type(path_string: str) -> str:
    return str(Path(path_string).resolve())
