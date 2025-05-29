from pathlib import Path
from src.interface import select_file_type, sort, sort_re, user_input_state, user_input_y_n, user_input_search



root_path = Path(__file__).resolve().parents[1]


if __name__ == "__main__":
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    transact = select_file_type()
    print(f"Введите статус, по которому необходимо выполнить фильтрацию."
          f"\nДоступные для фильтровки статусы: [E]XECUTED, [C]ANCELED, [P]ENDING.\n")
    user_state = user_input_state()
    transact = sort_re(transact, user_state, 'state')
    print("Отсортировать операции по дате? [Д]а/[Н]ет\n")
    yes_no = user_input_y_n()
    print("\nОтсортировать по возрастанию или по убыванию? По убыванию - [Д]а/По возрастанию - [Н]ет\n")
    user_reverse = user_input_y_n()
    transact = sort(transact, "date", user_reverse, yes_no)
    print("\nВыводить только рублевые транзакции? [Д]а/[Н]ет\n")
    yes_no = user_input_y_n()
    if yes_no == True:
        transact = sort_re(transact, "RUB", "currency_code")
    print("\nОтфильтровать список транзакций по определенному слову в описании? [Д]а/[Н]ет\n")
    yes_no = user_input_y_n()
    transact = user_input_search(transact, yes_no)
    for transaction in transact:
        print(transaction)
