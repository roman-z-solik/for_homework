from typing import Any, Dict, Generator


def filter_by_currency(transactions: dict, currency: str = "USD") -> Generator[Dict[str, Any], None, None]:
    """Функция filter_by_currency, которая принимает на вход список словарей, представляющих транзакции.
    Функция должна возвращать итератор, который поочередно выдает транзакции, где валюта операции
    соответствует заданной (например, USD)."""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield (transaction)


def transaction_descriptions(transactions: dict):  # type: ignore[no-untyped-def]
    """Генератор transaction_descriptions, который принимает список словарей
    с транзакциями и возвращает описание каждой операции по очереди."""
    for transaction in transactions:
        yield (transaction["description"])


def card_number_generator(start: int, stop: int) -> Generator:
    """Генератор card_number_generator, который выдает
    номера банковских карт в формате XXXX XXXX XXXX XXXX, где
    X — цифра номера карты. Генератор может сгенерировать номера карт
    в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999"""
    gen_numbers = range(start, stop)
    generated_num = [x for x in gen_numbers]
    card_number = "0000 0000 0000 0000"
    generated_card_number = ""
    generated_card_numbers = []
    if (
        not str(start).isdigit()
        or not str(stop).isdigit()
        or start < 0
        or stop < 0
        or start > 9999999999999999
        or stop > 10000000000000000
    ):
        raise TypeError("Введите число в диапазоне от 0 до 10000000000000000")
    while start <= stop:
        zeros_num = 16 - len(str(start))
        number_card_no_spaces = "0" * zeros_num + str(start)
        number_card = (
            f"{number_card_no_spaces[:4]} "
            f"{number_card_no_spaces[4:8]} "
            f"{number_card_no_spaces[8:12]} "
            f"{number_card_no_spaces[12:]}"
        )
        yield number_card
        start += 1
