import logging
import re
from pathlib import Path

from src.utils import read_csv_file, read_excel_file, read_json_file
from src.widget import get_date, mask_account_card

root_path = Path(__file__).resolve().parents[1]
logging.basicConfig(
    filename=f"{root_path}/logs/interface.log",
    encoding="utf-8",
    filemode="w",
    level=logging.DEBUG,
    format="%(asctime)s - %(filename)s - %(levelname)s: %(message)s",
)
logger_util = logging.getLogger()


def user_input_y_n() -> bool:
    """Функция, определяющая, ответил пользователь ДА или НЕТ на вопрос"""
    while True:
        user_input = input("Ввод: ")
        if (
            user_input.lower() == "lf"
            or user_input.lower() == "да"
            or user_input.lower() == "l"
            or user_input.lower() == "д"
        ):
            return True
        elif (
            user_input.lower() == "ytn"
            or user_input.lower() == "нет"
            or user_input.lower() == "y"
            or user_input.lower() == "н"
        ):
            return False
        else:
            print("Введите [Д]а или [Н]ет\n")


def import_data() -> list:
    """Функция предоставляет выбор пользователю, из какого файла импортировать
    данные о банковских операциях: JSON, CSV или XLSX и возвращает список транзакций"""
    text = """
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла
    """
    while True:
        type_input = input(f"{text}\nВвод: ")
        if type_input == "1":
            unsorted_data = read_json_file(f"{root_path}/data/operations.json")
            print("\nДля обработки выбран JSON файл.\n")
            data = sort_data_JSON(unsorted_data)
            return data
        if type_input == "2":
            unsorted_data = read_csv_file(f"{root_path}/data/transactions.csv")
            print("\nДля обработки выбран CSV файл.\n")
            data = sort_data_csv_xlsx(unsorted_data)
            return data
        if type_input == "3":
            unsorted_data = read_excel_file(f"{root_path}/data/transactions_excel.xlsx")
            print("\nДля обработки выбран Excel файл.\n")
            data = sort_data_csv_xlsx(unsorted_data)
            return data
        else:
            print("\nВыбран неверный пункт. Повторите ввод.")


def sort_data_JSON(data: list) -> list:
    """Приводит импортированные из JSON файла данные в нужный вид."""
    sorted_data = []
    for item in data:
        if item != {}:
            sorted_item = {}
            sorted_item["id"] = item["id"]
            sorted_item["state"] = item["state"]
            sorted_item["date"] = item["date"]
            sorted_item["amount"] = item["operationAmount"]["amount"]
            sorted_item["currency_name"] = item["operationAmount"]["currency"]["name"]
            sorted_item["currency_code"] = item["operationAmount"]["currency"]["code"]
            sorted_item["description"] = item["description"]
            try:
                sorted_item["from"] = mask_account_card(item["from"])
            except (KeyError, TypeError):
                sorted_item["from"] = ""
            try:
                sorted_item["to"] = mask_account_card(item["to"])
            except (KeyError, TypeError):
                continue
            sorted_data.append(sorted_item)
        else:
            continue
    return sorted_data


def sort_data_csv_xlsx(data: list) -> list:
    """Приводит импортированные из CSV или Excel файла данные в нужный вид."""
    sorted_data = []
    for item in data:
        sorted_item = {}
        sorted_item["id"] = item["id"]
        sorted_item["state"] = item["state"]
        sorted_item["date"] = item["date"]
        sorted_item["amount"] = item["amount"]
        if item["currency_name"] == "Ruble":
            sorted_item["currency_name"] = "руб."
        else:
            sorted_item["currency_name"] = item["currency_name"]
        sorted_item["currency_code"] = item["currency_code"]
        sorted_item["description"] = item["description"]
        try:
            sorted_item["from"] = mask_account_card(item["from"])
        except (KeyError, TypeError):
            sorted_item["from"] = ""
        try:
            sorted_item["to"] = mask_account_card(item["to"])
        except (KeyError, TypeError):
            continue
        sorted_data.append(sorted_item)
    return sorted_data


def input_sort_by_state() -> str:
    """Функция принимает ввод от пользователя, обозначающий статус,
    по которому необходимо выполнить фильтрацию. Доступные для фильтровки
    статусы: EXECUTED, CANCELED, PENDING"""
    print(
        "Введите статус, по которому необходимо выполнить фильтрацию."
        "\nДоступные для фильтровки статусы: [E]XECUTED, [C]ANCELED, [P]ENDING.\n"
    )
    while True:
        user_input = input("Ввод: ")
        if (
            user_input.lower() == "executed"
            or user_input.lower() == "e"
            or user_input.lower() == "t"
            or user_input == "у"
        ):
            user_state = "EXECUTED"
            print(f"\nОперации отфильтрованы по статусу {user_state}\n")
            return user_state
            break
        elif user_input.lower() == "canceled" or user_input.lower() == "c" or user_input.lower() == "с":
            user_state = "CANCELED"
            print(f"\nОперации отфильтрованы по статусу {user_state}\n")
            return user_state
            break
        elif (
            user_input.lower() == "pending"
            or user_input.lower() == "p"
            or user_input.lower() == "з"
            or user_input == "h"
        ):
            user_state = "PENDING"
            print(f"\nОперации отфильтрованы по статусу {user_state}\n")
            return user_state
            break
        else:
            print(f'\nСтатус операции "{user_input}" недоступен. Попробуйте ввести заново.\n')
            print(
                "Введите статус, по которому необходимо выполнить фильтрацию."
                "\nДоступные для фильтровки статусы: [E]XECUTED, [C]ANCELED, [P]ENDING.\n"
            )


def sort_re(transactions: list, sorted_value: str, sorted_item: str) -> list:
    """Функция принимает список словарей с данными о банковских операциях и данные для поиска,
    после чего возвращает список отсортированных с помощью библиотеки re словарей."""
    sorted_transactions = []
    for item in transactions:
        if re.findall(str(sorted_value), item[sorted_item], flags=re.IGNORECASE):
            sorted_transactions.append(item)
            # print(sorted_transactions)
    return sorted_transactions


def sort(transactions: list, sort_direction: bool, key_value: str) -> list:
    """Функция принимает список словарей с данными о банковских операциях, строку для сортировки,
    строку статуса реверса сортировки, сортирует список, после чего возвращает
    список словарей."""
    sorted_transactions = sorted(transactions, key=lambda transaction: transaction[key_value], reverse=sort_direction)
    return sorted_transactions


def count_categories(transactions: list) -> int:
    """Функция подсчета количества операций"""
    counted = [transaction["description"] for transaction in transactions]
    qty_operation = len(counted)
    return qty_operation


def print_result(transactions: list) -> None:
    """Выводит в консоль отсортированные готовые данные."""
    print("\nРаспечатываю итоговый список транзакций...\n")
    count = count_categories(transactions)
    if count == 0:
        print("\nНе найдено ни одной транзакции, \nподходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {count}\n")
    for item in transactions:
        date = get_date(item["date"])
        print(f"{date}  {item["description"]}")
        if item["from"] == "":
            print(f"{item["to"]}")
        else:
            print(f"{item["from"]} -> {item["to"]}")
        print(f"Сумма: {item["amount"]} {item["currency_name"]}\n")
