"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу
на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна
корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
class Division_null:
    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2

    @staticmethod
    def division_null(number_1, number_2):
        try:
            return (number_1 / number_2)
        except:
            return (f"На ноль делить нельзя")
print(Division_null.division_null(10, 0))
print(Division_null.division_null(10, 3))


