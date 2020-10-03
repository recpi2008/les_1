"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте
перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры
класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность
полученного результата.
"""
class ComplexNum:
    def __init__(self, num_1, num_2, *args):
        self.num_1 = num_1
        self.num_2 = num_2


    def __add__(self, next_num):
        return f'sum = {self.num_1 + next_num.num_1} + {self.num_2 + next_num.num_2} * j'

    def __mul__(self, next_num):
        return f'sum = {self.num_1 * next_num.num_1 - (self.num_2 * next_num.num_2)} + {self.num_2 * next_num.num_1} * j'

    def __str__(self):
        return f'sum = {self.num_1} + {self.num_2} * j'

my_num_1, my_num_2 = ComplexNum(10, 4), ComplexNum(43, 19)

print(my_num_1 + my_num_2)
print(my_num_1 * my_num_2)

