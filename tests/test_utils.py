from unittest.mock import Mock

from src.utils import read_csv_file, read_excel_file, read_json_file


def test_read_json_file(input_operations: dict) -> None:
    mock_transactions = Mock(return_value=input_operations)
    read_json_file = mock_transactions
    assert read_json_file() == input_operations
    read_json_file.assert_called_once_with()


def test_read_json_no_file() -> None:  # type: ignore[no-untyped-def]
    assert read_json_file("5.txt") == []


def test_read_csv_file(input_operations: dict) -> None:
    mock_transactions = Mock(return_value=input_operations)
    read_csv_file = mock_transactions
    assert read_csv_file() == input_operations
    read_csv_file.assert_called_once_with()


def test_read_csv_no_file() -> None:
    assert read_csv_file("5.txt") == []


def test_read_excel_file(input_operations: dict) -> None:
    mock_transactions = Mock(return_value=input_operations)
    read_excel_file = mock_transactions
    assert read_excel_file() == input_operations
    read_excel_file.assert_called_once_with()


def test_read_excel_no_file() -> None:
    assert read_excel_file("5.txt") == []
