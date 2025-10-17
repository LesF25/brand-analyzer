import pytest
from typing import Callable

from brand_analyzer.core.registry import Registry
from brand_analyzer.core.exceptions import (
    RegistryItemAlreadyExistsError,
    RegistryItemNotFoundError,
)
from brand_analyzer.core.file_reader import get_file_reader
from brand_analyzer.core.report_builder import get_report_builder


@pytest.fixture
def f_registry_name() -> str:
    return 'f_registry_name'


@pytest.fixture
def f_registry(f_registry_name: str) -> Registry:
    return Registry(f_registry_name)


def test_should_raise_registry_item_already_exists_error(
    monkeypatch: pytest.MonkeyPatch,
    f_registry: Registry,
    f_registry_name,
) -> None:
    f_key = 'fake_key'
    monkeypatch.setattr(
        f_registry,
        '_registry',
        {f_key: 'fake_value_1'}
    )

    with pytest.raises(RegistryItemAlreadyExistsError) as error:
        f_registry.add(f_key, 'fake_value_2')

    assert str(error.value) == (
        f"Item key='{f_key}' already exists in {f_registry_name}"
    )


@pytest.mark.parametrize(
    'registry_getter, expected_error_message', [
    (
        get_file_reader,
        'The file with the {!r} extension cannot be processed.',
    ),
    (
        get_report_builder,
        'The {!r} report does not exist.'
    ),
])
def test_should_raise_registry_item_not_found_error(
    registry_getter: Callable,
    expected_error_message: str,
) -> None:
    f_key = 'fake_key'

    with pytest.raises(RegistryItemNotFoundError) as error:
        registry_getter(f_key)

    assert str(error.value) == expected_error_message.format(f_key)


def test_registry(f_registry: Registry) -> None:
    f_registry.add('fake_key', 'fake_value')
    assert f_registry._registry == {'fake_key': 'fake_value'}
    assert f_registry.get('fake_key') == 'fake_value'
