import json
import logging
from pathlib import Path
from typing import Any

import pandas as pd

root_path = Path(__file__).resolve().parents[1]
logging.basicConfig(
    filename=f"{root_path}/logs/utils.log",
    encoding="utf-8",
    filemode="w",
    level=logging.DEBUG,
    format="%(asctime)s - %(filename)s - %(levelname)s: %(message)s",
)
logger_util = logging.getLogger()


def read_json_file(path_json: str) -> Any | list[dict[Any, Any] | Any | None]:
    """
    Функция, которая принимает JSON-файл из папки data
    и возвращает список словарей с данными о финансовых транзакциях
    """
    try:
        with open(path_json, "r", encoding="utf-8") as json_file:
            logger_util.info(f"Файл {path_json} корректно открыт")
            return json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError, PermissionError) as e:
        print(f"Ошибка чтения файла {path_json}: {str(e)}")
        logger_util.error(f"Ошибка чтения файла {path_json}: {str(e)}")
        return []


def read_csv_file(path_csv: str) -> Any | list[dict[Any, Any] | Any | None]:
    """
    Функция, которая принимает CSV-файл из папки data
    и возвращает список словарей с данными о финансовых транзакциях
    """
    try:
        with open(path_csv, "r", encoding="utf-8") as csv_file:
            logger_util.info(f"Файл {path_csv} корректно открыт")
            df = pd.read_csv(csv_file, delimiter=';')
            return df.to_dict(orient="records")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Ошибка чтения файла {path_csv}: {str(e)}")
        logger_util.error(f"Ошибка чтения файла {path_csv}: {str(e)}")
        return []


def read_excel_file(path_xls: str) -> Any | list[dict[Any, Any] | Any | None]:
    """
    Функция для считывания финансовых операций из Excel, принимает путь к файлу Excel в качестве аргумента.
    """
    try:
        with open(path_xls, "rb") as excel_file:
            logger_util.info(f"Файл {path_xls} корректно открыт")
            df = pd.read_excel(excel_file)
            return df.to_dict(orient="records")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Ошибка при чтении файла {path_xls}: {str(e)}")
        return []

# if __name__ == '__main__':
#     try:
#         result = read_json_file(f'{root_path}/data/operations.json')
#         for item in result:
#             print(item['state'])
#     except KeyError:
#         print('None')
#     # print(result['state'])
#     # print(result)

# if __name__ == '__main__':
#     csv_file = read_csv_file(f'{root_path}/data/transactions.csv')
#     print(csv_file)
#     print(type(csv_file))

# if __name__ == '__main__':
#     print(read_excel_file(f'{root_path}/data/transactions_excel.xlsx'))
