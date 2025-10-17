from typing import Callable, Any

from app.core.registry import get_report_builder_registry


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

    return report_builder_type()
