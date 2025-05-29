from pathlib import Path
from src.interface import select_file_type, sort, sort_re
from src.interface import user_input_state, user_input_y_n, user_input_search, count_categories, result_output

root_path = Path(__file__).resolve().parents[1]

if __name__ == "__main__":
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    transact = select_file_type()
    print(
        "Введите статус, по которому необходимо выполнить фильтрацию."
        "\nДоступные для фильтровки статусы: [E]XECUTED, [C]ANCELED, [P]ENDING.\n"
    )
    user_state = user_input_state()
    transact = sort_re(transact, user_state, 'state')
    print("Отсортировать операции по дате? [Д]а/[Н]ет\n")
    yes_no = user_input_y_n()
    print("\nОтсортировать по возрастанию или по убыванию? По убыванию - [Д]а/По возрастанию - [Н]ет\n")
    user_reverse = user_input_y_n()
    transact = sort(transact, "date", user_reverse, yes_no)
    print("\nВыводить только рублевые транзакции? [Д]а/[Н]ет\n")
    yes_no = user_input_y_n()
    if yes_no:
        transact = sort_re(transact, "RUB", "currency_code")
    print("\nОтфильтровать список транзакций по определенному слову в описании? [Д]а/[Н]ет\n")
    yes_no = user_input_y_n()
    transact = user_input_search(transact, yes_no)
    print("\nРаспечатываю итоговый список транзакций...\n")
    count = count_categories(transact)
    if count == 0:
        print("\nНе найдено ни одной транзакции, \nподходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {count}\n")
        result = result_output(transact)
    for item in result:
        if item["description"] == "Открытие вклада":
            print(f"{item["date"]} {item["description"]}\n{item["from"]}{item["to"]}")
        else:
            print(f"{item["date"]} {item["description"]}\n{item["from"]} -> {item["to"]}")
