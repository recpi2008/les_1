"""
Поработайте с переменными, создайте несколько,
выведите на экран, запросите у пользователя несколько чисел и строк
и сохраните в переменные, выведите на экран.
"""

myname = "Иван"
print("Привет, меня зовут", myname)
ask_name = "Как тебя зовут?\n"
name = input(ask_name)
print("Привет", name)
my_one = 9
my_two = 3
print(f"Я выбрал два числа {my_one} и {my_two}")
ask_one = " Теперь твоя очередь. Введи первое число\n"
ask_two = "Введи второе число\n"
first_number = int(input(ask_one))
second_number = int(input(ask_two))
print(f"Ты выбрал числа {first_number} и {second_number}.")
c = my_one + my_two + first_number + second_number
print("Сумма наших с тобой чисел =", c)