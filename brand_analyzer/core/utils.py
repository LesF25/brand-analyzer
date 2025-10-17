from typing import Any, Callable
from functools import wraps
from pathlib import Path

from brand_analyzer.core.exceptions import (
    RegistryItemNotFoundError,
    RegistryItemAlreadyExistsError,
)


def resolve_path_type(path_string: str) -> str:
    return str(Path(path_string).resolve())


def handle_error(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(
        *args: Any,
        **kwargs: Any,
    ) -> Any:
        try:
            return func(*args, **kwargs)
        except FileNotFoundError as error:
            print(
                'File not found. Please check the file name and its location: '
                f'{error.filename}.'
            )

        except (
            RegistryItemAlreadyExistsError,
            RegistryItemNotFoundError,
        ) as error:
            print(str(error))

    return wrapper
