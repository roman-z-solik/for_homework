import logging
import re
from pathlib import Path

from src.utils import read_csv_file, read_excel_file, read_json_file
from tests.conftest import transactions

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
    text = """
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
"""
    while True:
        type_input = input(f"{text}\nВвод: ")
        if type_input == "1":
            print(f"\nДля обработки выбран JSON файл.\n")
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
            print(f"\nВыбран неверный пункт. Повторите ввод.")


def user_input_state() -> str:
    while True:
        user_input = input("Ввод: ")
        if user_input.lower() == "executed" or user_input.lower() == "e" or user_input.lower() == "у":
            user_state = "EXECUTED"
            print(f"\nОперации отфильтрованы по статусу {user_state}\n")
            return(user_state)
            break
        elif user_input.lower() == "canceled" or user_input.lower() == "c" or user_input.lower() == "с":
            user_state = "CANCELED"
            print(f"\nОперации отфильтрованы по статусу {user_state}\n")
            return (user_state)
            break
        elif user_input.lower() == "pending" or user_input.lower() == "p" or user_input.lower() == "з":
            user_state = "PENDING"
            print(f"\nОперации отфильтрованы по статусу {user_state}\n")
            return (user_state)
            break
        else:
            print(f"\nСтатус операции \"{user_input}\" недоступен. Попробуйте ввести заново.\n")


def sort_re(transactions: list, sorted_value:str, sorted_item:str) -> list:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска,
    после чего возвращает список словарей, у которых в описании есть данная строка"""
    sorted_transactions_state = []
    for item in transactions:
        try:
            if re.findall(str(sorted_value), item[sorted_item], flags=re.IGNORECASE):
                sorted_transactions_state.append(item)
        except (TypeError,KeyError) as e:
            logger_util.info(f"{e} ошибка")
    return (sorted_transactions_state)


def sort(transactions: list, key_value:str, reverse:bool, status:bool) -> list:
    """Функция принимает список словарей с данными о банковских операциях, строку для сортировки,
        строку статуса для реверса сортировки, сортирует список, после чего возвращает
        список словарей"""
    if status == True:
        sorted_transactions = sorted(transactions, key=lambda transaction: transaction[key_value], reverse = reverse)
        return (sorted_transactions)
    else:
        return(transactions)


def user_input_y_n() -> bool:
    """Функция, которая отпределяет, оветил пользователь ДА или НЕТ на вопрос"""
    user_input = input("Ввод: ")
    if user_input.lower() == "lf" or user_input.lower() == "да" or user_input.lower() == "l" or user_input.lower() == "д":
        return(True)
    else:
        return(False)


def user_input_search(transactions, yes_no):
    if yes_no == True:
        search_value = input("\nВведите строку для поиска: ")
        print(search_value)
        sorted_transactions = sort_re(transactions, search_value.upper(), "description")
        print("Отсортировано!")
        return (sorted_transactions)
    else:
        return (transactions)
