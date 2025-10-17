import pytest
from unittest import mock

from .report_builder import AverageRatingReportBuilder


@pytest.fixture
def f_file_name() -> str:
    return 'f_file_name'


@pytest.fixture
def m_reader() -> mock.Mock:
    reader = mock.Mock()
    reader.read_file.return_value = [
        {'model': 'f_model_1', 'brand': 'f_brand_1', 'rating': 2},
        {'model': 'f_model_2', 'brand': 'f_brand_1', 'rating': 1.5},
        {'model': 'f_model_3', 'brand': 'f_brand_2', 'rating': 1},
    ]

    return reader


@pytest.fixture
def m_get_file_reader(m_reader) -> mock.Mock:
    with mock.patch('src.reports.average_rating.report_builder.get_file_reader') as m:
        m.return_value = m_reader

        yield m


@pytest.mark.usefixtures('m_get_file_reader')
def test_build_report(
    f_file_name: str,
) -> None:
    report_builder = AverageRatingReportBuilder()

    assert report_builder.report([f_file_name]) == [
        {'brand': 'f_brand_1', 'rating': 1.75},
        {'brand': 'f_brand_2', 'rating': 1},
    ]
