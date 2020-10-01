"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
 К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
 параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
 соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на
реальных данных. Реализовать общий подсчет расхода ткани. Проверить на практике полученные
на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
 проверить на практике работу декоратора @property.
"""
class Сlothes:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def square_coat(self):
        return self.size / 6.5 + 0.5

    def square_suit(self):
        return self.height * 2 + 0.3

    @property
    def general_square(self):
        return str(f'Общий расход ткани \n'
                   f' {(self.size / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Сlothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.coat_square = round(self.size / 6.5 + 0.5)

    def __str__(self):
        return f'Расход ткани на пальто {self.coat_square}'


class Suit(Сlothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.suit_square = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Расход ткани на костюм {self.suit_square}'

coat = Coat(3, 5)
suit = Suit(2, 4)
print(coat)
print(suit)
print(suit.general_square)
