import re
import logging

from pathlib import Path
from typing import Any

from src.utils import read_json_file, read_csv_file, read_excel_file

root_path = Path(__file__).resolve().parents[1]
logging.basicConfig(
    filename=f"{root_path}/logs/interface.log",
    encoding="utf-8",
    filemode="w",
    level=logging.DEBUG,
    format="%(asctime)s - %(filename)s - %(levelname)s: %(message)s",
)
logger_util = logging.getLogger()


def select_transaction_for_type() -> Any | list[dict[Any, Any] | Any | None]:
    text = """
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
"""
    while True:
        type_input = input(f"""{text}
Ввод: """)
        if type_input  == "1":
            result_json = []
            print("Для обработки выбран JSON файл.")
            json_read_file = read_json_file(f'{root_path}/data/operations.json')
            print(json_read_file)
            try:
                for item in json_read_file:
                    if item['state'].lower() in ["executed", "canceled", "pending"]:
                        result_json.append(item)
            except KeyError as e:
                 logger_util.info(f"{e} ошибка")
            return (result_json)
            # return(read_json_file(f'{root_path}/data/operations.json'))
            break
        elif type_input == "2":
            print("Для обработки выбран CSV файл.")
            return (read_csv_file(f'{root_path}/data/transactions.csv'))
            break
        elif type_input == "3":
            print("Для обработки выбран Excel файл.")
            return(read_excel_file(f'{root_path}/data/transactions_excel.xlsx'))
            break
        else:
            print("Выбран неверный пункт. Повторите ввод.")


def select_transaction_for_status(transactions:list) -> list:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска,
    после чего возвращает список словарей, у которых в описании есть данная строка"""
    text = """
Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING."""
    user_input = input(f"""{text}
Ввод: """)
    selected_transactions = []
    while True:
        if user_input.lower() not in ["executed", "canceled", "pending"]:
            print(f"""
Статус операции "{user_input}" недоступен. Попробуйте ввести заново.""")
            user_input = input(f"""{text} '
Ввод: """)
        else:
            for item in transactions:
                try:
                    if re.findall(str(user_input), item['state'], flags=re.IGNORECASE):
                        selected_transactions.append(item)
                except TypeError:
                    continue
            return f"""Операции отфильтрованы по статусу {user_input.upper()}
{selected_transactions}"""


# transactions = select_transaction_for_type()
# result = select_transaction_for_status(transactions)
# print(result)

# result = select_transaction_for_type()
# print(result)
