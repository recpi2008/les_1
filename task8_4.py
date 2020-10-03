"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс
«Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники
(принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""
class Warehouse:

    def __init__(self, name, price, quantity, *args):
        self.name = name
        self.price = price
        self.quantity = quantity

        self.warehouse = []
        self.store = []
        self.model = {'Модель': self.name, 'Стоимомть ': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} стоимомть {self.price} количество {self.quantity}'

    def reception(self):
        try:
            user_model = input(f'Введите оргтехнику:')
            model_price = int(input(f'Введите стоимость:'))
            model_quantity = int(input(f'Введите количество:'))
            personal = {'Модель устройства': user_model, 'Стоимость': model_price, 'Количество': model_quantity}
            self.model.update(personal)
            self.store.append(self.model)
            print(f'Текущий список: {self.store}')
        except:
            return f'Не правильный ввод'
        user_num = input(f'Для выхода списка всего склада "C", для продолжения ввода оргтехники любую клавишу:')
        user_num = user_num.lower()
        if user_num == 'c':
            self.warehouse.append(self.store)
            print(f'Весь склад -\n {self.warehouse}')
            return f'Выход'
        else:
            return Warehouse.reception(self)

class Printer(Warehouse):
    def printer(self):
        return f'to print smth {self.numb} times'

class Scanner(Warehouse):
    def scanner(self):
        return f'to scan smth {self.numb} times'

class Copier(Warehouse):
    def copier(self):
        return f'to copier smth  {self.numb} times'

model_1 = Printer('Xerox Phaser', 6538, 9)
model_2 = Scanner('Canon CanoScan', 5040, 15)
model_3 = Copier('KYOCERA', 35900, 17)
print(model_1.reception(), model_2.reception(), model_3.reception())
print(model_1.printer(), model_2.scanner(), model_3.copier())
