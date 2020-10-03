"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
«день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен
извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной
структуры на реальных данных.
"""
class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        given_date = []

        for i in day_month_year.split():
            if i != '-': given_date.append(i)

        return int(given_date[0]), int(given_date[1]), int(given_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 <= year <= 2020:
                    return f'Все отлично'
                else:
                    return f'Некоректный год'
            else:
                return f'Некоректный месяц'
        else:
            return f'Некоректный день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


today = Data('03 - 10 - 2020')
print(today)
print(Data.valid(11, 11, 2050))
print(today.valid(11, 13, 2011))
print(Data.valid(5, 10, 2020))