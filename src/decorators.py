from functools import wraps


def log(filename=None):  # type: ignore[no-untyped-def]
    """Декоратор log принимает необязательный аргумент filename,
    который определяет имя файла, в который будут записываться логи.
    Если filename не задан, то логи выводятся в консоль. Если вызов функции
    закончился ошибкой, записывается сообщение об ошибке и входные параметры функции"""

    def decorator(func):  # type: ignore[no-untyped-def]
        @wraps(func)
        def wrapper(*args, **kwargs):  # type: ignore[no-untyped-def]
            try:
                result = func(*args, **kwargs)
                if filename is None:
                    print(f"{func.__name__} ok")
                else:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} ok\n")

            except Exception as e:
                result = None
                if filename is None:
                    print(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
                else:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}\n")

            return result

        return wrapper

    return decorator
