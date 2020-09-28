"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color,
name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar,
SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать
текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Выполните вызов методов и также покажите результат.
"""
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} тронулся'
    def stop(self):
        return f'{self.name} остановился'
    def left_turn(self):
        return f'{self.name} повернул налево'
    def right_turn(self):
        return f'{self.name} повернул направо'
    def show_speed(self):
        return f'скорость  {self.name} состовляет {self.speed}'

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f' скорость {self.name} составляет {self.speed}')
        if self.speed > 40:
            return f'{self.name} превысил скорость в городе'
        else:
            return f'{self.name} движется с нормальной скоростью'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'текущая скорость {self.name} составляет {self.speed}')

        if self.speed > 60:
            return f' {self.name} превысил скорость'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} полицейчкая машина'
        else:
            return f'{self.name} не полицейчкая машина'

jeep, mercedes, buggy, peugeot = WorkCar(90, 'black', 'Jeep', True), TownCar(40, 'Red', 'Mercedes', False), SportCar(200, 'Purle', 'Buggy', False), PoliceCar(110, 'Blue',  'Peugeot', True)

print(mercedes.go(),'и', buggy.right_turn())
print(f'{buggy.right_turn()}, после {jeep.stop()}')
print(mercedes.show_speed(), {mercedes.color} )
print(f'{jeep.go()},{jeep.show_speed()}, {jeep.name} - это полицейская машина? {jeep.is_police}')
