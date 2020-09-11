"""
Пользователь вводит время в секундах. Переведите время в часы,
минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""
while True:
    ask_sec = input("Введи количество секунд\n")
    if ask_sec.isdigit():
        sec_user = int(ask_sec)
        break
    print("Вы ввели не число. Повторите ввод")
hour, min, sec = sec_user // 3600, (sec_user // 60) % 60, sec_user % 60
print(f"{hour:>02}:{min:>02}:{sec:>02}")
