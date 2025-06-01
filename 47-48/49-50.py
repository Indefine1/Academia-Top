from datetime import datetime
from rich.console import Console
from rich.table import Table
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

    def max_price_number(self, top_n=5):
        if not self.catalogs:
            print("Список покупок пуст.")
            return []
        return sorted(self.catalogs, key=lambda x: x['price'], reverse=True)[:top_n]


class RichView:
    def __init__(self):
        self.console = Console()

    def show_catalogs(self, catalogs):
        table = Table(title='Список покупок')
        table.add_column('Номер', justify='center', style="red")
        table.add_column('Продукт', justify='center', style="blue")
        table.add_column('Цена', justify='center', style="green")
        table.add_column('Время', justify='center', style="blue")

        if not catalogs:
            table.add_row("", "Список покупок пуст", "", "")
        else:
            for number, item in enumerate(catalogs, start=1):
                table.add_row(str(number), item['product'], str(item['price']), item['time'])
        self.console.print(table)


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_buy(self, _add_buy, add_price):
        self.model.add_catalog(_add_buy, add_price)

    def view_catalog(self):
        self.view.show_catalogs(self.model.catalogs)

    def max_price(self):
        top_items = self.model.max_price_number()
        if top_items:
            print(f"\nТоп-5 самых дорогих покупок:")
            for i, item in enumerate(top_items, 1):
                print(f"{i}. {item['product']} - {item['price']} руб. (Время: {item['time']})")


richview = RichView()
model = Model()
controller = Controller(model, richview)

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