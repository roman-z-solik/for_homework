def get_mask_card_number(card_number: str) -> str:
    '''Функция, возвращающая маску введенного номера карты'''
    mask_card_number = str(f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}")
    return mask_card_number


def get_mask_account(account_number: str) -> str:
    '''Функция, возвращающая маску введенного номера счета'''
    mask_account_number = str(f"**{account_number[-4:]}")
    return mask_account_number
