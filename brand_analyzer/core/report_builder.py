from typing import Callable, Any

from brand_analyzer.core.registry import get_report_builder_registry
from brand_analyzer.core.exceptions import RegistryItemNotFoundError


class ReportBuilder:
    def report(self, files: list[str]) -> list[dict[str, Any]]:
        raise NotImplemented()


def report_builder(
    report_type: str,
) -> Callable[[type[ReportBuilder]], type[ReportBuilder]]:
    def fn_wrapper(cls: type[ReportBuilder]) -> type[ReportBuilder]:
        registry = get_report_builder_registry()

        registry.add(report_type, cls)

        return cls

    return fn_wrapper


def get_report_builder(report_type: str) -> ReportBuilder:
    registry = get_report_builder_registry()
    report_builder_type = registry.get(report_type)

    if report_builder_type is None:
        raise RegistryItemNotFoundError(
            f'The {report_type!r} report does not exist.'
        )

    return report_builder_type()
