import json


def read_json_file(path_json: str) -> list[dict | None]:
    """
    Функция, которая принимает JSON-файл из папки data
    и возвращает список словарей с данными о финансовых транзакциях
    """
    try:
        with open(path_json, "r", encoding="utf-8") as json_file:
            return json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError, PermissionError) as e:
        print(f"Ошибка при чтении файла {path_json}: {str(e)}")
        return []


# if __name__ == '__main__':
#     print(read_json_file('D:/PythonProject/widget-bank/data/operations.json'))
