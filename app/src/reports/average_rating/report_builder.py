from pathlib import Path
from collections import defaultdict
from typing import Any, Generator

from app.core.file_readers import get_file_reader
from app.core.report_builder import ReportBuilder, report_builder
from ..constants import ReportBuilderType
from .structures import AverageData


@report_builder(ReportBuilderType.AVERAGE_RATING)
class AverageRatingReportBuilder(ReportBuilder):
    def report(self, files: list[str]) -> list[dict[str, Any]]:
        result = defaultdict(AverageData)

        for file in files:
            for row in self._get_rows(file):
                average_data = result[row['brand']]
                average_data.count += 1
                average_data.rating += float(row['rating'])

        data = [
            {
                'brand': brand,
                'rating': (average_data.rating / average_data.count),
            }
            for brand, average_data in result.items()
        ]

        return data

    def _get_rows(self, file_name: str) -> Generator[dict[str, Any], None, None]:
        reader = get_file_reader(
            ''.join(Path(file_name).suffixes)
        )

        for row in reader.read_file(file_name):
            yield row
