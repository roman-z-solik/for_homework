import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("7000792289606362", "7000 79** **** 6362"),
        ("0400792289606361", "0400 79** **** 6361"),
    ],
)
def test_get_mask_card_number(card_number, expected):  # type: ignore[no-untyped-def]
    assert get_mask_card_number(card_number) == expected


def test_get_mask_wrong_card_number(wrong_card_number):  # type: ignore[no-untyped-def]
    with pytest.raises(AssertionError):
        get_mask_card_number(wrong_card_number)


def test_get_mask_zero_card_number():  # type: ignore[no-untyped-def]
    with pytest.raises(AssertionError):
        get_mask_card_number("")


@pytest.mark.parametrize(
    "account_number, expected",
    [("73654108430135874305", "**4305"), ("73654108430135874304", "**4304"), ("03654108430135874300", "**4300")],
)
def test_get_mask_account(account_number, expected):  # type: ignore[no-untyped-def]
    assert get_mask_account(account_number) == expected


def test_get_mask_wrong_account_number(wrong_account_number):  # type: ignore[no-untyped-def]
    with pytest.raises(AssertionError):
        get_mask_account(wrong_account_number)


def test_get_mask_zero_account_number():  # type: ignore[no-untyped-def]
    with pytest.raises(AssertionError):
        get_mask_account("")
