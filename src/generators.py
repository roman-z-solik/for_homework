transactions = (
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)

def filter_by_currency(transactions:dict, currency:str="USD"):
    current_currency = currency
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == current_currency:
            yield (transaction)


def transaction_descriptions(transactions:dict):
    for transaction in transactions:
        yield (transaction["description"])


def card_number_generator(start:int, end:int):
    gen_numbers = range(start, end)
    generated_num = [x for x in gen_numbers]
    card_number = "0000 0000 0000 0000"
    generated_card_number = ""
    generated_card_numbers = []
    # return(generated_num)
    for num in generated_num:
        if num < 10:
            generated_card_number = card_number[:-1]+str(num)
            generated_card_numbers.append(generated_card_number)
        elif num < 100:
            generated_card_number = card_number[:-2] + str(num)
            generated_card_numbers.append(generated_card_number)
        elif num < 1000:
            generated_card_number = card_number[:-3] + str(num)
            generated_card_numbers.append(generated_card_number)
        elif num < 10000:
            generated_card_number = card_number[:-4] + str(num)
            generated_card_numbers.append(generated_card_number)
        elif num < 100000:
            generated_card_number = card_number[:-6] + str(num)[-5] + " " + str(num)[-4:]
            generated_card_numbers.append(generated_card_number)
        elif num < 1000000:
            generated_card_number = card_number[:-7] + str(num)[-6:-4] + " " + str(num)[-4:]
            generated_card_numbers.append(generated_card_number)
        elif num < 10000000:
            generated_card_number = card_number[:-8] + str(num)[-7:-4] + " " + str(num)[-4:]
            generated_card_numbers.append(generated_card_number)
        elif num < 100000000:
            generated_card_number = card_number[:-9] + str(num)[-8:-4] + " " + str(num)[-4:]
            generated_card_numbers.append(generated_card_number)
        elif num < 1000000000:
            generated_card_number = card_number[:-11] + str(num)[-9] + " " + str(num)[-8:-4] + " " + str(num)[-4:]
            generated_card_numbers.append(generated_card_number)
        elif num < 10000000000:
            generated_card_number = card_number[:-12] + str(num)[-11:-8] + " " + str(num)[-8:-4] + " " + str(num)[-4:]
            generated_card_numbers.append(generated_card_number)
        elif num < 100000000000:
            generated_card_number = card_number[:-13] + str(num)[-12:-8] + " " + str(num)[-8:-4] + " " + str(num)[-4:]
            generated_card_numbers.append(generated_card_number)
        elif num < 1000000000000:
            generated_card_number = card_number[:-14] + str(num)[-13:-8] + " " + str(num)[-8:-4] + " " + str(num)[-4:]
            generated_card_numbers.append(generated_card_number)
        elif num < 10000000000000:
            generated_card_number = card_number[:3] + str(num)[-13] + " " + str(num)[-12:-8] + " " + str(num)[-8:-4] + " " + str(num)[-4:]
            generated_card_numbers.append(generated_card_number)
        elif num < 100000000000000:
            generated_card_number = card_number[:2] + str(num)[-14:-12] + " " + str(num)[-12:-8] + " " + str(num)[-8:-4] + " " + str(num)[-4:]
            generated_card_numbers.append(generated_card_number)
        elif num < 1000000000000000:
            generated_card_number = card_number[:1] + str(num)[-15:-12] + " " + str(num)[-12:-8] + " " + str(num)[-8:-4] + " " + str(num)[-4:]
            generated_card_numbers.append(generated_card_number)
        elif num < 10000000000000000:
            generated_card_number = str(num)[-16:-12] + " " + str(num)[-12:-8] + " " + str(num)[-8:-4] + " " + str(num)[-4:]
            generated_card_numbers.append(generated_card_number)

    return (generated_card_numbers)







# usd_transactions = filter_by_currency(transactions, "USD")
# try:
#     for _ in range(4):
#         print(next(usd_transactions))
# except:
#     print("End Of File")
# descriptions = transaction_descriptions(transactions)
# for _ in range(5):
#     print(next(descriptions))
for card_number in card_number_generator(9999999999999995, 9999999999999999):
    print(card_number)