import csv
from typing import Any, Generator

from ..schemas import File


class CsvReader:
    def read_file(
        self,
        files: list[File],
    ) -> Generator[dict[str, Any], None, None]:
        for file in files:
            yield from self._process_file(file.file_name)

    def _process_file(
        self,
        file_name: str
    ) -> Generator[dict[str, Any], None, None]:
        with open(file_name, mode='r') as file:
            for row in csv.DictReader(file):
                yield row
