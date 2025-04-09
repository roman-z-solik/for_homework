from masks import get_mask_card_number, get_mask_account

def mask_account_card(user_payment_method: str) -> str:
    """Функция возвращает строку с замаскированным номером счета или карты.
    Для карт и счетов используются разные маски из модуля masks"""
    # print(user_payment_method)
    if user_payment_method[:4] == "Счет":
        return (user_payment_method[:4] + " " + get_mask_account(user_payment_method[-20:]))
    else:
        return(user_payment_method[:-16] + " " + get_mask_card_number(user_payment_method[-16:]))


def get_date(user_date: str) -> str:
    """Функция, которая принимает на вход дату
       и возвращает её в формате ДД.ММ.ГГГГ"""
    return(f"{user_date[8:10]}.{user_date[5:7]}.{user_date[:4]}")