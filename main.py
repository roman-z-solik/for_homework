from pathlib import Path
from src.interface import select_transaction_for_type, select_transaction_for_status

root_path = Path(__file__).resolve().parents[1]


if __name__ == "__main__":
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    select_transactions = select_transaction_for_type()
    # print(select_transactions)
    # print(type(select_transactions))
    sorted_transactions = select_transaction_for_status(select_transactions)
    print(sorted_transactions)