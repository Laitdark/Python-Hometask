import os
import json

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


def write_order_to_json(item, quantity, price, buyer, date):
    filename = os.path.join(CURRENT_DIR, 'source_data', 'orders.json')

    if os.path.exists(filename):
        data = {}

        with open(filename, encoding="utf-8") as fl:
            data = json.loads(fl.read())

        data['orders'].append({'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date})

        with open(filename, "w", encoding="utf-8") as fl:
            json.dump(data, fl, indent=4, separators=(',', ': '), ensure_ascii=False)

        print(f'Данные добавлены в {filename}')

    else:
        print(f'Исходный файл по пути {filename} не найден')


if __name__ == '__main__':
    write_order_to_json('Книга', '1', '200', 'Попов', '22.02.2022')
    write_order_to_json('Листы бумаги', '1', '100', 'Иванов', '22.02.2022')