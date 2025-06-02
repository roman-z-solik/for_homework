from unittest.mock import Mock

from src.interface import count_categories, sort, sort_re


def test_sort_data_JSON(sorted_transactions: list) -> None:
    mock_transactions = Mock(return_value=sorted_transactions)
    sort_data_JSON = mock_transactions
    assert sort_data_JSON() == sorted_transactions
    sort_data_JSON.assert_called_once_with()


def test_data_csv_xlsx(sorted_transactions: list) -> None:
    mock_transactions = Mock(return_value=sorted_transactions)
    sort_data_csv_xlsx = mock_transactions
    assert sort_data_csv_xlsx() == sorted_transactions
    sort_data_csv_xlsx.assert_called_once_with()


def test_sort_re(sorted_transactions_by_state: list) -> None:
    assert sort_re(sorted_transactions_by_state, "EXECUTED", "state") == [
        {
            "id": 2177828.0,
            "state": "EXECUTED",
            "date": "2022-04-14T15:14:21Z",
            "amount": 24853.0,
            "currency_name": "Yuan Renminbi",
            "currency_code": "CNY",
            "from": "Счет 38577962752140632721",
            "to": "Счет 47657753885349826314",
            "description": "Перевод со счета на счет",
        }
    ]


def test_sort_re_empty(sorted_transactions_by_state: list) -> None:
    assert sort_re([], "EXECUTED", "state") == []


def test_sort(sorted_transactions_by_state: list) -> None:
    assert sort(sorted_transactions_by_state, False, "date") == [
        {
            "id": 214410.0,
            "state": "PENDING",
            "date": "2020-10-29T09:56:28Z",
            "amount": 34336.0,
            "currency_name": "Krona",
            "currency_code": "SEK",
            "from": "Discover 6590095029387674",
            "to": "Mastercard 0974688087552673",
            "description": "Перевод с карты на карту",
        },
        {
            "id": 4699552.0,
            "state": "CANCELED",
            "date": "2021-03-23T08:29:37Z",
            "amount": 23423.0,
            "currency_name": "Peso",
            "currency_code": "PHP",
            "from": "Discover 7269000803370165",
            "to": "American Express 1963030970727681",
            "description": "Перевод с карты на карту",
        },
        {
            "id": 2177828.0,
            "state": "EXECUTED",
            "date": "2022-04-14T15:14:21Z",
            "amount": 24853.0,
            "currency_name": "Yuan Renminbi",
            "currency_code": "CNY",
            "from": "Счет 38577962752140632721",
            "to": "Счет 47657753885349826314",
            "description": "Перевод со счета на счет",
        },
    ]


def test_sort_empty(sorted_transactions_by_state: list) -> None:
    assert sort([], True, "state") == []


def test_count_categories(sorted_transactions_by_state: list) -> None:
    assert count_categories(sorted_transactions_by_state) == 3
