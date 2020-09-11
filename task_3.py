"""
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например,
пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""
while True:
    ask_n = input("Введите число:\n")
    if ask_n.isdigit():
        n_user = int(ask_n)
        break
    print("Вы ввели не число. Повторите ввод.")
tmp = str(n_user)
second_tmp = tmp + tmp
third_tmp = tmp + tmp + tmp
answer = n_user + int(second_tmp) + int(third_tmp)
print(f"Сумма чисел: {n_user} + {second_tmp} + {third_tmp} = {answer}")
"""
#short solution
answer = n_user + int(n_user*2) + int(n_user*3)

"""