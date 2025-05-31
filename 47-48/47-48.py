from datetime import datetime
import json

class Model:
    def __init__(self):
        self.catalogs = []
        self.load_json_catalog()

    def load_json_catalog(self):
        try:
            with open('logs.json', 'r', encoding='utf-8') as f:
                self.catalogs = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.catalogs = []

    def add_catalog(self, _add_buy, add_price):
        dtime = datetime.now()
        self.catalogs.append({
            'product': _add_buy,
            'price': add_price,
            'time': dtime.strftime('%Y/%m/%d %H:%M:%S')
        })
        with open('logs.json', 'w', encoding='utf-8') as f:
            json.dump(self.catalogs, f, ensure_ascii=False, indent=4)

    def view(self):
        if not self.catalogs:
            print("Список покупок пуст.")
            return
        for product in self.catalogs:
            print(f"Наименование товара: {product['product']}. Цена: {product['price']} руб. Время: {product['time']}")

    def max_price_number(self, top_n=5):
        if not self.catalogs:
            print("Список покупок пуст.")
            return
        sorted_items = sorted(self.catalogs, key=lambda x: x['price'], reverse=True)
        print(f"\nТоп-{top_n} самых дорогих покупок:")
        for i, item in enumerate(sorted_items[:top_n], 1):
            print(f"{i}. {item['product']} - {item['price']} руб. (Время: {item['time']})")


class Controller:
    def __init__(self, model):
        self.model = model

    def add_buy(self, _add_buy, add_price):
        self.model.add_catalog(_add_buy, add_price)

    def view_catalog(self):
        self.model.view()

    def max_price(self):
        self.model.max_price_number()


model = Model()
controller = Controller(model)

while True:
    print('\nМеню:\n1. Добавить покупку.\n2. Показать все покупки.\n3. Показать 5 самых дорогих покупок.\n4. Выход')
    ans = input('Выберите действие: ')
    if ans == '1':
        _add_buy = input('Введите название покупки: ')
        add_price = int(input('Введите стоимость покупки: '))
        controller.add_buy(_add_buy, add_price)
    elif ans == '2':
        controller.view_catalog()
    elif ans == '3':
        controller.max_price()
    elif ans == '4':
        print("Выход из программы.")
        break
    else:
        print("Неверный ввод. Попробуйте снова.")



