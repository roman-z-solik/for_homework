import logging
from pathlib import Path

root_path = Path(__file__).resolve().parents[1]
logging.basicConfig(
    filename=f"{root_path}/logs/masks.log",
    encoding="utf-8",
    filemode="w",
    level=logging.DEBUG,
    format="%(asctime)s - %(filename)s - %(levelname)s: %(message)s",
)
logger_card = logging.getLogger()
logger_account = logging.getLogger()


def get_mask_card_number(card_number: str) -> str:
    """Функция, возвращающая маску введенного номера карты"""
    card_number = str(card_number)
    logger_card.info(f"Получена карта: {card_number}")
    if not str(card_number).isdigit():
        logger_card.error("Номер карты должен состоять только из цифр")
        raise AssertionError("Номер карты должен состоять только из цифр")
    if len(str(card_number)) == 0:
        logger_card.error("Номер карты не может быть пустым")
        raise AssertionError("Номер карты не может быть пустым")
    if len(str(card_number)) != 16:
        logger_card.error("Номер карты должен состоять из 16 цифр")
        raise AssertionError("Номер карты должен состоять из 16 цифр")
    mask_card_number = str(f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}")
    logger_card.info(f"Маска карты: {mask_card_number} сформирована корректно")
    return mask_card_number


def get_mask_account(account_number: str) -> str:
    """Функция, возвращающая маску введенного номера счета"""
    logger_account.info(f"Получен счет: {account_number}")
    if len(str(account_number)) != 20:
        logger_account.error("Номер счета должен состоять из 20 цифр")
        raise AssertionError("Номер счета должен состоять из 20 цифр")
    if len(str(account_number)) == 0:
        logger_account.error("Номер счета не может быть пустым")
        raise AssertionError("Номер счета не может быть пустым")
    if not str(account_number).isdigit():
        logger_account.error("Номер счета должен состоять только из цифр")
        raise AssertionError("Номер счета должен состоять только из цифр")
    mask_account_number = str(f"**{account_number[-4:]}")
    logger_account.info(f"Маска счета: {mask_account_number} сформирован корректно")
    return mask_account_number
