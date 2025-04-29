import pytest


@pytest.fixture
def wrong_card_number() -> tuple:
    return (700079228960636112, "700079228960636248", "adv0636248", "0400792289606", "7228960636112")


@pytest.fixture
def wrong_account_number() -> tuple:
    return (12212700079228960636112, "121212700079228960636248", "adv0636248", "0400792289606", 7228960636112)


@pytest.fixture
def wrong_user_payment_method() -> tuple:
    return (
        "Maestro 1596837705199",
        "Счет 45353830334744478560",
        "Счет 353adv0636248",
        "0400792289606",
        "Visa Gold 64686473678894779589",
    )


@pytest.fixture
def wrong_user_date() -> tuple:
    return (
        "2026-03-11T02:26:18.671407",
        "2abcdT02:26:18.671407",
        "2023-15-11T02:26:18.671407",
        "2022-03-58T02:26:18.671407",
        "20240311T02:26:18.671407",
    )
