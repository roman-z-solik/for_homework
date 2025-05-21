import json
import logging
from pathlib import Path
from typing import Any

root_path = Path(__file__).resolve().parents[1]
logging.basicConfig(
    filename=f"{root_path}/logs/utils.log",
    encoding="utf-8",
    filemode="w",
    level=logging.DEBUG,
    format="%(asctime)s - %(filename)s - %(levelname)s: %(message)s",
)
logger_util = logging.getLogger()


def read_json_file(path_json: str) -> Any | list[dict[Any, Any] | Any | None]:  # type: ignore[no-untyped-def]
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
