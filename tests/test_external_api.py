from unittest.mock import Mock, patch

from src.external_api import currency_conversions


def test_currency_conversions_rub(input_operations_in_rub):  # type: ignore[no-untyped-def]
    result = currency_conversions(input_operations_in_rub)
    assert result == "31957.58"


@patch("src.external_api.requests.get")
def test_currency_conversions_usd(mock_get, input_operations_in_usd):  # type: ignore[no-untyped-def]
    mock_response = Mock()
    mock_response.json.return_value = {"result": 7500.50}
    mock_get.return_value = mock_response
    result = currency_conversions(input_operations_in_usd)
    assert result == 7500.50


def test_currency_conversions_invalid_data():  # type: ignore[no-untyped-def]
    assert currency_conversions({}) is None
    assert currency_conversions({"operationAmount": {}}) is None
