from masks import get_mask_card_number, get_mask_account

def mask_account_card(user_payment_method: str) -> str:
    """Функция возвращает строку с замаскированным номером счета или карты.
    Для карт и счетов используются разные маски из модуля masks"""
    # print(user_payment_method)
    if user_payment_method[:4] == "Счет":
        return (user_payment_method[:4] + " " + get_mask_account(user_payment_method[-20:]))
    else:
        return(user_payment_method[:-16] + " " + get_mask_card_number(user_payment_method[-16:]))

# print(mask_account_card("Счет 64686473678894779589"))
# print(mask_account_card("Maestro 1596837868705199"))
# print(mask_account_card("MasterCard 7158300734726758"))
# print(mask_account_card("Счет 35383033474447895560"))
# print(mask_account_card("Visa Classic 6831982476737658"))
# print(mask_account_card("Visa Platinum 8990922113665229"))
# print(mask_account_card("Visa Gold 5999414228426353"))
# print(mask_account_card("Счет 73654108430135874305"))
#print(get_date("2023-12-23T02:26:18.671407"))