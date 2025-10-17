import argparse
from collections import defaultdict

from tabulate import tabulate

from src.adapters import CsvReader
from src.constants import ReportType
from src.schemas import AverageData, CommandArguments


class Application:
    def __init__(self):
        self._parser = argparse.ArgumentParser(
            description='Analyzes the rating of files by csv files'
        )
        self._register_command()

    @classmethod
    def run(cls) -> None:
        instance = cls()
        args = CommandArguments(**instance.parse_args().__dict__)

        if args.report == ReportType.AVERAGE_RATING:
            result = defaultdict(AverageData)

            adapter = CsvReader()
            for row in adapter.read_file(args.files):
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

            table = tabulate(
                data,
                headers='keys',
                numalign='right',
                floatfmt='.2f',
                showindex='always',
                tablefmt="grid",
            )

            print(table)

            return

        raise ValueError(
            f"The report type {args.command} doesn't exist."
        )

    def parse_args(self) -> argparse.Namespace:
        return self._parser.parse_args()

    def _register_command(self) -> None:
        self._parser.add_argument(
            '--files',
            nargs='*',
            required=True,
            help='Paths to the input files.',
        )
        self._parser.add_argument(
            '--report',
            required=True,
            help='The report type to generate.',
        )

        return


if __name__ == '__main__':
    try:
        Application.run()
    except KeyboardInterrupt:
        ...
