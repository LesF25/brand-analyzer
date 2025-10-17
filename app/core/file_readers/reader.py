from typing import Generator, Callable, Any, TypeAlias

from app.core.registry import get_file_reader_registry

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

    return file_reader_type()
