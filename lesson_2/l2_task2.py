"""
Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
Написать скрипт, автоматизирующий его заполнение данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря
в файл orders.json. При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""
import json
from datetime import date


def write_order_to_json(item, quantity, price, buyer, date):
    json_data = {
        "orders":
            [
                item,
                quantity,
                price,
                buyer,
                date
            ]
    }
    with open('orders.json', 'w') as orders_file:
        json.dump(json_data, orders_file,indent=4)


if __name__ == '__main__':

    item_name = 'product'
    qty = 5
    price = 1050.73
    buyer_name = 'John Doe'
    date_now = date.today().strftime("%d.%m.%Y")

    try:
        with open('orders.json') as before:
            print(f'Содержание файла до перезаписи: {json.load(before)}\n'
                  f'-----------------------------------------------------')
    except json.decoder.JSONDecodeError:
        print(f'Чтение файла до перезаписи: файл пуст!\n'
              f'------------')

    write_order_to_json(item_name, qty, price, buyer_name, date_now)

    try:
        with open('orders.json') as after:
            print(f'Содержание файла после перезаписи: {json.load(after)}\n'
                  f'-----------------------------------------------------')
    except json.decoder.JSONDecodeError:
        print(f'Файл пуст!\n'
              f'------------')
