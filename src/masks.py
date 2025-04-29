def get_mask_card_number(card_number: str) -> str:
    """Функция, возвращающая маску введенного номера карты"""
    card_number = str(card_number)
    if not str(card_number).isdigit():
        raise AssertionError("Номер карты должен состоять только из цифр")
    if len(str(card_number)) == 0:
        raise AssertionError("Номер карты не может быть пустым")
    if len(str(card_number)) != 16:
        raise AssertionError("Номер карты должен состоять из 16 цифр")
    mask_card_number = str(f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}")
    return mask_card_number


def get_mask_account(account_number: str) -> str:
    """Функция, возвращающая маску введенного номера счета"""
    if len(str(account_number)) != 20:
        raise AssertionError("Номер счета должен состоять из 20 цифр")
    if len(str(account_number)) == 0:
        raise AssertionError("Номер счета не может быть пустым")
    if not str(account_number).isdigit():
        raise AssertionError("Номер счета должен состоять только из цифр")
    mask_account_number = str(f"**{account_number[-4:]}")
    return mask_account_number
