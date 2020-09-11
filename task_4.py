"""
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""
while True:
    ask_n = input("Введите целое положительное число:")
    if ask_n.isdigit():
        n_user = int(ask_n)
        break
    print("Вы ввели не число. Повторите ввод.")
temp = n_user
tmp = temp % 10
temp = temp // 10
while temp > 0:
    if temp % 10 > tmp:
        tmp = temp % 10
    temp = temp//10
print("Самая большая цифра из вашего числа", tmp)