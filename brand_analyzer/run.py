import argparse

from tabulate import tabulate

from brand_analyzer import src
from brand_analyzer.core.report_builder import get_report_builder
from brand_analyzer.core.structures import CommandArguments
from brand_analyzer.core.utils import resolve_path_type, handle_error


class Application:
    def __init__(self):
        self._parser = argparse.ArgumentParser(
            description='Analyzes the rating of files by csv files'
        )
        self._register_command()

    @classmethod
    @handle_error
    def run(cls) -> None:
        instance = cls()
        args = CommandArguments(**instance.parse_args().__dict__)

        report_builder = get_report_builder(args.report)

        table = tabulate(
            report_builder.report(args.files),
            headers='keys',
            numalign='right',
            floatfmt='.2f',
            showindex='always',
            tablefmt="grid",
        )

        print(table)

    def parse_args(self) -> argparse.Namespace:
        return self._parser.parse_args()

    def _register_command(self) -> None:
        self._parser.add_argument(
            '--files',
            nargs='*',
            required=True,
            help='Paths to the input files.',
            type=resolve_path_type,
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
