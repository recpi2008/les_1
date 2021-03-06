"""
Спортсмен занимается ежедневными пробежками. В первый день его
# результат составил a километров. Каждый день спортсмен увеличивал результат
# на 10 % относительно предыдущего. Требуется определить номер дня, на который
# общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число
 — номер дня.
"""
while True:
    a = input("Введите сколько км вы пробежали в первый день:\n")
    if a.isdigit():
        a = int(a)
        break
    print("Вы ввели не число. Повторите ввод.")
while True:
    b = input("Введите общий результат в км:\n")
    if b.isdigit():
        b = int(b)
        break
    print("Вы ввели не число. Повторите ввод.")
quantity_km = a
quantity_day = 1
while quantity_km < b:
    quantity_day += 1
    quantity_km = quantity_km + quantity_km * 0.1
    print(f"В {quantity_day} день вы пробежите {quantity_km:.2f} км")
print("Ваша цель будет достигнута на %d день" % (quantity_day))