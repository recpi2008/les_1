"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы
с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
"""
my_list = [15, 12, 9, 8, 3]
print(f"Рейтинг - {my_list}")
while True:
    ask_n = input("Введите число для рейтинга:")
    if ask_n.isdigit():
        user_num = int(ask_n)
        break
    print("Вы ввели не число. Повторите ввод.")
for el in range(len(my_list)):
    if my_list[el] > user_num and my_list[el + 1] < user_num:
        my_list.insert(el+1, user_num) #new_num
        break
    elif my_list[-1] > user_num: # last_ind
        my_list.append(user_num)
    elif my_list[0] < user_num: # first_ind
        my_list.insert(0, user_num)
    elif my_list[el] == user_num:
        my_list.insert(el + 1, user_num) #same_num
        break
print(f"текущий список - {my_list}")
