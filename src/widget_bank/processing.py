input_operations = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(input_operations: list, state: str = "EXECUTED") -> list:
    """Функция принимает список словарей и опционально значение для ключа
    state (по умолчанию EXECUTED). Dозвращает новый список словарей,
    содержащий только те словари, у которых ключ state
    соответствует указанному значению."""
    output_operations = []
    for operation in input_operations:
        if operation["state"] == state:
            output_operations.append(operation)
        else:
            continue
    return output_operations
