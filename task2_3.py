"""
Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года
относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
"""
while True:
    ask_n = input("Введите месяц в виде целого числа: ")
    if ask_n.isdigit():
        month = int(ask_n)
        if 1 <= month <= 12:
            break
    print("Такого месяца не существует. Повторите ввод.")
seasons_list = ["Зима", "Весна", "Лето", "Осень"]
seasons_dict = {1 : "Зима", 2 : "Весна", 3 : "Лето", 4 : "Осень"}
if 1 <= month <= 2 or month == 12:
        print(f"{month} месяц это - {seasons_dict.get(1)}")
elif 3 <= month <= 5:
    print(f"{month} месяц это - {seasons_dict.get(2)}")
elif 6 <= month <= 8:
    print(f"{month} месяц это - {seasons_dict.get(3)}")
elif 9 <= month <= 11:
    print(f"{month} месяц это - {seasons_dict.get(4)}")

"""
#other decision from teacher
user_month_num = 12
seson_idx = user_month_num // 3 % 4
for key, value in seasons_dict.items():
    if user_month_num in value:
        print(key)
        break
print(seson_idx)
print(seasons_list[seson_idx])
"""



