from pathlib import Path

import pytest

from .csv_reader import CsvReader


@pytest.fixture
def f_file_path() -> str:
    current_path = Path(__file__).parent.resolve()
    return str(current_path / 'fixtures' / 'f_csv_file.csv')


def test_csv_reader(
    f_file_path: str,
) -> None:
    reader = CsvReader()
    generator = reader.read_file(f_file_path)

    assert list(generator) == [
        {'name': 'iphone 15 pro', 'brand': 'apple', 'price': '999', 'rating': '4.9'},
        {'name': 'galaxy s23 ultra', 'brand': 'samsung', 'price': '1199', 'rating': '4.8'},
        {'name': 'redmi note 12', 'brand': 'xiaomi', 'price': '199', 'rating': '4.6'},
        {'name': 'iphone 14', 'brand': 'apple', 'price': '799', 'rating': '4.7'},
        {'name': 'galaxy a54', 'brand': 'samsung', 'price': '349', 'rating': '4.2'},
    ]
