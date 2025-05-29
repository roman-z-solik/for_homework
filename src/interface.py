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


def select_file_type() -> list:
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
            print("\nДля обработки выбран JSON файл.\n")
            json_read_file = read_json_file(f"{root_path}/data/operations.json")
            return json_read_file
            break
        elif type_input == "2":
            print("\nДля обработки выбран CSV файл.\n")
            return read_csv_file(f"{root_path}/data/transactions.csv")
            break
        elif type_input == "3":
            print("\nДля обработки выбран Excel файл.\n")
            return read_excel_file(f"{root_path}/data/transactions_excel.xlsx")
            break
        else:
            print("\nВыбран неверный пункт. Повторите ввод.")


def user_input_state() -> str:
    """Функция принимает ввод от пользователя, обозначающий статус,
    по которому необходимо выполнить фильтрацию. Доступные для фильтровки
    статусы: EXECUTED, CANCELED, PENDING"""
    while True:
        user_input = input("Ввод: ")
        if user_input.lower() == "executed" or user_input.lower() == "e" or user_input.lower() == "у":
            user_state = "EXECUTED"
            print(f"\nОперации отфильтрованы по статусу {user_state}\n")
            return user_state
            break
        elif user_input.lower() == "canceled" or user_input.lower() == "c" or user_input.lower() == "с":
            user_state = "CANCELED"
            print(f"\nОперации отфильтрованы по статусу {user_state}\n")
            return user_state
            break
        elif user_input.lower() == "pending" or user_input.lower() == "p" or user_input.lower() == "з":
            user_state = "PENDING"
            print(f"\nОперации отфильтрованы по статусу {user_state}\n")
            return user_state
            break
        else:
            print(f'\nСтатус операции "{user_input}" недоступен. Попробуйте ввести заново.\n')


def sort_re(transactions: list, sorted_value: str, sorted_item: str) -> list:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска,
    после чего возвращает список словарей, у которых в описании есть данная строка"""
    sorted_transactions_state = []
    for item in transactions:
        try:
            if re.findall(str(sorted_value), item[sorted_item], flags=re.IGNORECASE):
                sorted_transactions_state.append(item)
        except (TypeError, KeyError) as e:
            logger_util.info(f"{e} ошибка")
    return sorted_transactions_state


def sort(transactions: list, key_value: str, reverse: bool, status: bool) -> list:
    """Функция принимает список словарей с данными о банковских операциях, строку для сортировки,
    строку статуса для реверса сортировки, сортирует список, после чего возвращает
    список словарей."""
    if status:
        sorted_transactions = sorted(transactions, key=lambda transaction: transaction[key_value], reverse=reverse)
        return sorted_transactions
    else:
        return transactions


def user_input_y_n() -> bool:
    """Функция, отпределяющая, оветил пользователь ДА или НЕТ на вопрос"""
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
            print("\nВведите [Д]а или [Н]ет\n")


def user_input_search(transactions: list, yes_no: bool) -> list:
    """Функция поиска определяемой пользователем строки в списке транзакций,
    и выдает отсортированный список по запросу пользователяuser_input_search"""
    if yes_no:
        search_value = input("\nИщем транзакции по определенному слову.\nВведите строку для поиска: ")
        sorted_transactions = sort_re(transactions, search_value.upper(), "description")
        return sorted_transactions
    else:
        return transactions


def count_categories(transactions: list) -> int:
    """Функция подсчета операций по категориям."""
    counted = [transaction["description"] for transaction in transactions]
    qty_operation = len(counted)
    return qty_operation


def result_output(transactions: list) -> list:
    """Формирование окончательного вывода согласно задания."""
    result_list: list = []
    for item in transactions:
        result_item = {}
        date = get_date(item["date"])
        result_item["date"] = date
        description = item["description"]
        result_item["description"] = description
        if description == "Открытие вклада":
            result_item["to"] = mask_account_card(item["to"])
            result_item["from"] = ""
        else:
            result_item["to"] = mask_account_card(item["to"])
            result_item["from"] = mask_account_card(item["from"])
        result_list.append(result_item)
    return result_list
