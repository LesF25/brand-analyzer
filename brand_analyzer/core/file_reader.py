from typing import Generator, Callable, Any, TypeAlias

from brand_analyzer.core.registry import get_file_reader_registry
from brand_analyzer.core.exceptions import RegistryItemNotFoundError

FileReaderType: TypeAlias = type['BaseFileReader']


class BaseFileReader:
    def read_file(
        self,
        file_name: str,
    ) -> Generator[dict[str, Any], None, None]:
        raise NotImplemented()


def file_reader(
    file_extension: str,
) -> Callable[[FileReaderType], FileReaderType]:
    def fn_wrapper(cls: FileReaderType) -> FileReaderType:
        registry = get_file_reader_registry()

        registry.add(file_extension, cls)

        return cls

    return fn_wrapper


def get_file_reader(extension: str) -> BaseFileReader:
    registry = get_file_reader_registry()
    file_reader_type = registry.get(extension)

    if file_reader_type is None:
        raise RegistryItemNotFoundError(
            f'The file with the {extension!r} extension cannot be processed.'
        )

    return file_reader_type()
