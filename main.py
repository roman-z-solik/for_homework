from src.interface import import_data, user_input_y_n, input_sort_by_state, sort_re
from src.interface import sort, count_categories, print_result

if __name__ == "__main__":
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    transact = import_data()
    user_state = input_sort_by_state()
    transact = sort_re(transact, user_state, 'state')
    print("Отсортировать операции по дате? [Д]а/[Н]ет")
    sort_date = user_input_y_n()
    if sort_date:
        print("Отсортировать по возрастанию или по убыванию? По убыванию - [Д]а/По возрастанию - [Н]ет")
        direction = user_input_y_n()
        transact = sort (transact, direction, "date")
    print("\nВыводить только рублевые транзакции? [Д]а/[Н]ет")
    yes_no = user_input_y_n()
    if yes_no:
        transact = sort_re(transact, "RUB", "currency_code")
    print("\nОтфильтровать список транзакций по определенному слову в описании? [Д]а/[Н]ет")
    yes_no = user_input_y_n()
    if yes_no:
        search_value = input("Ищем транзакции по определенному слову.\nВведите строку для поиска: ")
        transact = sort_re(transact, search_value, "description")
    print_result(transact)
