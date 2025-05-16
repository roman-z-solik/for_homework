from unittest.mock import Mock
from src.utils import read_json_file
import pytest


def test_read_json_file(input_operations):
    mock_transactions = Mock(return_value=input_operations)
    read_json_file = mock_transactions
    assert read_json_file() == input_operations
    read_json_file.assert_called_once_with()


def test_read_json_no_file():
    assert read_json_file("1") == []
