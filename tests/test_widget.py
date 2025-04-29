import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "user_payment_method, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(user_payment_method, expected):
    assert mask_account_card(user_payment_method) == expected


def test_wrong_account_card(wrong_user_payment_method):
    with pytest.raises(AssertionError):
        mask_account_card(wrong_user_payment_method)


def test_zero_account_card():
    with pytest.raises(AssertionError):
        mask_account_card("")


@pytest.mark.parametrize(
    "user_date, expected",
    [("2024-03-11T02:26:18.671407", "11.03.2024"), ("2025-12-05T02:26:18.671407", "05.12.2025")],
)
def test_get_date(user_date, expected):
    assert get_date(user_date) == expected


def test_zero_get_date():
    with pytest.raises(AssertionError):
        get_date("")


def test_wrong_user_date(wrong_user_date):
    with pytest.raises(AttributeError):
        get_date(wrong_user_date)
