Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv
script_name, all_hour, rate, prize = argv
all_hour = int(all_hour)
rate = int(rate)
prize = int(prize)
def salary_func():
    # all_hour выработка в часах
    # rate ставка в час
    # prize премия
    all_salary = all_hour * rate + prize
    return all_salary
user_dict = {"Выработка в часах: ": all_hour, "Ставка в час: ": rate, "Премия: ": prize}
print(user_dict)
print("Итоговая зарплата сотрудника: ", salary_func())
# C:\Users\recpi\OneDrive\Рабочий стол\PythonMy\Lesson_1_myself>python script_salary.py
