"""
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например,
пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

n_user = int(input("Введите число:"))
tmp = str(n_user)
second_tmp = tmp + tmp
third_tmp = tmp + tmp + tmp
answer = n_user + int(second_tmp) + int(third_tmp)
print(f"Сумма чисел: {n_user} + {second_tmp} + {third_tmp} = {answer}")