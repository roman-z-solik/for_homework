from unittest.mock import Mock

from src.utils import read_json_file


def test_read_json_file(input_operations: dict):  # type: ignore[no-untyped-def]
    mock_transactions = Mock(return_value=input_operations)
    read_json_file = mock_transactions
    assert read_json_file() == input_operations
    read_json_file.assert_called_once_with()


def test_read_json_no_file() -> None:  # type: ignore[no-untyped-def]
    assert read_json_file("1") == []
