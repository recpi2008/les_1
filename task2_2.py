"""
Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы
 с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
 Для заполнения списка элементов необходимо использовать функцию input().
"""

while True:
    ask_n = input("Введите количество элементов в списке:")
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


"""
#fast decision from teacher
user_answer = input("Введите список через запятую")
user_list = user_answer.split(",")

idx = 0
while idx < len(user_list) - 1:
    user_list[idx], user_list[idx+1] = user_list[idx+1], user_list[idx]
    idx += 2
print(user_list)
"""
"""
#decision from teacher
product_template = {
    "Название": ("Название товара", str),
    "Цена": ("Стоимость товара", int),
    "Количество": ("Количество товара", int),
    "Еденицы": ("Единицы измерения", str)
}
next_enter = True

auto_inc = 1
products_list = []

while next_enter:
    #словарь в который запосляем атрибуты товара
    product = {}
    #заполняем товар по шаблону
    for key, value in product_template.items():
        #цикл while True для того чтобы повторить вопрос при неверном вводе по типу
        while True:
            user_value = input(f"{value[0]}")
            try:
                user_value = value[1](user_value) #int (user_value)
            except ValueError as e:
                print(f"{e} \n Не верное значение данных")
                continue
            product[key] = user_value
            break
    products_list.append((auto_inc, product))
    auto_inc += 1
    #проверяем нужно ли ещу вводить товар
    while True:
        next_add = input("Добавить еще продукт? Да/Нет\n")
        if next_add.lower() in ("Да","Нет"):
            next_enter = next_add.lower() == "Да"
            break
        else:
            print("Неверный ввод. Повторите")
print(products_list)

product_alalytics = {}
# собираем словарь аналитики
for key in product_template:
    resalt = []
    for itm in products_list:
        resalt.append(itm[1][key])
    product_alalytics[key] = resalt

print(product_alalytics)
"""


