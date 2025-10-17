import argparse

from tabulate import tabulate

from app import src
from app.core.report_builder import get_report_builder
from app.core.structures import CommandArguments
from app.core.utils import resolve_path_type


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

        report_builder = get_report_builder(args.report)

        try:
            data = report_builder.report(args.files)
        except FileNotFoundError as error:
            print(
                f'File not found. Please check the file name and its location: '
                f'{error.filename or 'Unknown file'}.'
            )

            return

        table = tabulate(
            data,
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
