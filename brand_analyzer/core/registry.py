from typing import Any, Hashable, Optional

from .exceptions import RegistryItemAlreadyExistsError


class Registry:
    def __init__(
        self,
        name: str,
    ) -> None:
        self._name = name
        self._registry = {}

    def add(
        self,
        key: Hashable,
        value: Any
    ) -> None:
        if key in self._registry:
            raise RegistryItemAlreadyExistsError(
                f'Item {key=!r} already exists in {self._name}'
            )

        self._registry[key] = value

    def get(self, key: Hashable) -> Optional[Any]:
        return self._registry.get(key)

    def __contains__(self, key: Hashable) -> bool:
        return key in self._registry


__report_builder = Registry('ReportBuilder')


def get_report_builder_registry() -> Registry:
    return __report_builder


__file_reader = Registry('FileReader')


def get_file_reader_registry() -> Registry:
    return __file_reader
