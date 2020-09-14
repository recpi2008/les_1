"""
Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы
 с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
 Для заполнения списка элементов необходимо использовать функцию input().
"""
while True:
    ask_n = input("Введите целое положительное число:")
    if ask_n.isdigit():
        quantity_inlist = int(ask_n)
        break
    print("Вы ввели не число. Повторите ввод.")
user_list = []
n = 0
while n < quantity_inlist:
    user_list.append(input(f"Введите {n + 1} значение списка "))
    n += 1
print(f"Ваш исходный список {user_list}")
a = 0
for el in range(int(len(user_list)/2)):
        user_list[a], user_list[a + 1] = user_list [a + 1], user_list[a]
        a += 2
print(f"Преобразованный список {user_list}")