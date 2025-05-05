import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions):  # type: ignore[no-untyped-def]
    generator = filter_by_currency(transactions, "USD")
    assert next(generator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(generator) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }


def test_filter_by_wrong_currency(transactions):  # type: ignore[no-untyped-def]
    generator = filter_by_currency(transactions, "EUR")
    with pytest.raises(StopIteration):
        next(generator)


def test_empty_transaction() -> None:  # type: ignore[no-untyped-def]
    generator = filter_by_currency([], "USD")
    with pytest.raises(StopIteration):
        next(generator)


def test_transaction_descriptions(transactions):  # type: ignore[no-untyped-def]
    generator = transaction_descriptions(transactions)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод с карты на карту"
    assert next(generator) == "Перевод организации"


def test_transaction_descriptions_with_empty_transaction() -> None:
    generator = transaction_descriptions([])
    with pytest.raises(StopIteration):
        next(generator)


@pytest.fixture
def start_for_generator():  # type: ignore[no-untyped-def]
    return 1


@pytest.fixture
def stop_for_generator():  # type: ignore[no-untyped-def]
    return 5


def test_card_number_generator(start_for_generator: int, stop_for_generator: int):  # type: ignore[no-untyped-def]
    generator = card_number_generator(start_for_generator, stop_for_generator)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"


@pytest.fixture
def start_for_generator1() -> int:
    return 9999999999999995


@pytest.fixture
def stop_for_generator1() -> int:  # type: ignore[no-untyped-def]
    return 10000000000000000


def test_card_number_generator1(start_for_generator1: int, stop_for_generator1: int):  # type: ignore[no-untyped-def]
    generator = card_number_generator(start_for_generator1, stop_for_generator1)
    assert next(generator) == "9999 9999 9999 9995"
    assert next(generator) == "9999 9999 9999 9996"
    assert next(generator) == "9999 9999 9999 9997"
    assert next(generator) == "9999 9999 9999 9998"
    assert next(generator) == "9999 9999 9999 9999"


@pytest.mark.parametrize(
    "start, stop",
    [(-10, 2), (1, -2), (99999999999999991, 2), ("start", 115), (10, "end")],
)
def test_card_number_generator_with_wrong_range(start, stop):  # type: ignore[no-untyped-def]
    generator = card_number_generator(start, stop)
    with pytest.raises(TypeError):
        next(generator)
