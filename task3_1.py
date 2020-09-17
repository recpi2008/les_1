"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""
while True:
    user_num_1 = input("Введите первое число: ")
    user_num_2 = input("Введите второе число: ")
    if user_num_1.isdigit() and user_num_2.isdigit():
        num_1 = int(user_num_1)
        num_2 = int(user_num_2)
        break
    print("Вы ввели не число. Повторите ввод.")
def cal_del(num_1,num_2):
    try:
        res_del = num_1 / num_2
    except ZeroDivisionError:
        return "На ноль делить нельзя"
    return res_del
answer_del = cal_del(num_1,num_2)
print(f"Частное Ваших чисел: {answer_del:.2f} ")

