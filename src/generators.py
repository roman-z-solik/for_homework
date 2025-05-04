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
    for num in generated_num:
        if num < 10:
            generated_card_number = card_number[:-1] + str(num)
            generated_card_numbers.append(generated_card_number)
        elif num < 100:
            generated_card_number = card_number[:-2] + str(num)
            generated_card_numbers.append(generated_card_number)
        elif num < 1000:
            generated_card_number = card_number[:-3] + str(num)
            generated_card_numbers.append(generated_card_number)
        elif num < 10000:
            generated_card_number = card_number[:-4] + str(num)
            generated_card_numbers.append(generated_card_number)
        elif num < 100000:
            generated_card_number = card_number[:-6] + str(num)[-5] + " " + str(num)[-4:]
            generated_card_numbers.append(generated_card_number)
        elif num < 1000000:
            generated_card_number = card_number[:-7] + str(num)[-6:-4] + " " + str(num)[-4:]
            generated_card_numbers.append(generated_card_number)
        elif num < 10000000:
            generated_card_number = card_number[:-8] + str(num)[-7:-4] + " " + str(num)[-4:]
            generated_card_numbers.append(generated_card_number)
        elif num < 100000000:
            generated_card_number = card_number[:-9] + str(num)[-8:-4] + " " + str(num)[-4:]
            generated_card_numbers.append(generated_card_number)
        elif num < 1000000000:
            generated_card_number = card_number[:-11] + str(num)[-9] + " " + str(num)[-8:-4] + " " + str(num)[-4:]
            generated_card_numbers.append(generated_card_number)
        elif num < 10000000000:
            generated_card_number = card_number[:-12] + str(num)[-11:-8] + " " + str(num)[-8:-4] + " " + str(num)[-4:]
            generated_card_numbers.append(generated_card_number)
        elif num < 100000000000:
            generated_card_number = card_number[:-13] + str(num)[-12:-8] + " " + str(num)[-8:-4] + " " + str(num)[-4:]
            generated_card_numbers.append(generated_card_number)
        elif num < 1000000000000:
            generated_card_number = card_number[:-14] + str(num)[-13:-8] + " " + str(num)[-8:-4] + " " + str(num)[-4:]
            generated_card_numbers.append(generated_card_number)
        elif num < 10000000000000:
            generated_card_number = (
                card_number[:3] + str(num)[-13] + " " + str(num)[-12:-8] + " " + str(num)[-8:-4] + " " + str(num)[-4:]
            )
            generated_card_numbers.append(generated_card_number)
        elif num < 100000000000000:
            generated_card_number = (
                card_number[:2]
                + str(num)[-14:-12]
                + " "
                + str(num)[-12:-8]
                + " "
                + str(num)[-8:-4]
                + " "
                + str(num)[-4:]
            )
            generated_card_numbers.append(generated_card_number)
        elif num < 1000000000000000:
            generated_card_number = (
                card_number[:1]
                + str(num)[-15:-12]
                + " "
                + str(num)[-12:-8]
                + " "
                + str(num)[-8:-4]
                + " "
                + str(num)[-4:]
            )
            generated_card_numbers.append(generated_card_number)
        elif num < 10000000000000000:
            generated_card_number = (
                str(num)[-16:-12] + " " + str(num)[-12:-8] + " " + str(num)[-8:-4] + " " + str(num)[-4:]
            )
            generated_card_numbers.append(generated_card_number)

    for generated_card_number in generated_card_numbers:
        yield (generated_card_number)
