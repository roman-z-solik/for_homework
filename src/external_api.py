import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("APILAYER_API_KEY")


def currency_conversions(transaction: dict) -> float | None | Any:
    """Функция, которая возвращает сумму транзакции в рублях"""
    try:
        if not transaction:
            print("В словаре нет данных")

        currency_data = transaction.get("operationAmount", {}).get("currency", {})
        if currency_data.get("code") == "RUB":
            return transaction["operationAmount"]["amount"]

        currency = currency_data.get("code")
        amount = transaction["operationAmount"].get("amount")

        if not currency or not amount:
            print("Ошибка данных")

        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        headers = {"apikey": api_key}
        response = requests.get(url, headers=headers, timeout=10)
        return round(response.json()["result"], 2)
    except requests.exceptions.RequestException as e:
        return f"Ошибка API: {e}"
    except (KeyError, TypeError) as e:
        return f"Ошибка данных транзакции: {e}"
