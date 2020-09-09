"""
Пользователь вводит время в секундах. Переведите время в часы,
минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

ask_sec = "Введи количество секунд\n"
sec_user = int(input(ask_sec))
hour = sec_user // 3600
min = (sec_user // 60) % 60
sec = sec_user % 60
if hour<10:
    hour = str("0" + str(hour))
else:
    hour = str(hour)
if min < 10:
    min = str("0" + str(min))
else:
    min = str(min)
if sec<10:
    sec = str("0" + str(sec))
else:
    sec = str(sec)

print(f"{hour}:{min}:{sec}")