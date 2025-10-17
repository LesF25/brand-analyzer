import csv
from typing import Any, Generator

from brand_analyzer.core.file_reader import file_reader, BaseFileReader


@file_reader('.csv')
class CsvReader(BaseFileReader):
    def read_file(
        self,
        file_name: str,
    ) -> Generator[dict[str, Any], None, None]:
        with open(file_name, mode='r') as file:
            for row in csv.DictReader(file):
                yield row
