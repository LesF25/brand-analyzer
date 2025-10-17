import pytest

from app.core.registry import (
    Registry,
    RegistryItemAlreadyExistsError,
    RegistryItemNotFoundError
)


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


def test_should_raise_registry_item_not_found_error(
    monkeypatch: pytest.MonkeyPatch,
    f_registry: Registry,
    f_registry_name,
) -> None:
    f_key = 'fake_key'
    monkeypatch.setattr(f_registry, '_registry', {})

    with pytest.raises(RegistryItemNotFoundError) as error:
        f_registry.get(f_key)

    assert str(error.value) == (
        f"Item with key='{f_key}' doesn't exists!"
    )


def test_registry(f_registry: Registry) -> None:
    f_registry.add('fake_key', 'fake_value')
    assert f_registry._registry == {'fake_key': 'fake_value'}
    assert f_registry.get('fake_key') == 'fake_value'
