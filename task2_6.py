"""
Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара
 и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения). Структуру
  нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
например название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""
total = []
user_template = {"Название": "", "Цена": "", "Колличество": "", "Еденица измерения": ""}
analytic_list = {"Название": [], "Цена": [], "Колличество": [], "Еденица измерения": []}
num = 0
user = None
control = None
while True:
    num += 1
    for ask in user_template.keys():
        user = input(f"Введите '{ask}'")
        user_template[ask] = int(user) if (ask == "Цена" or ask == "Колличество") else user
        analytic_list[ask].append(user_template[ask])
    total.append((num, user_template))
    while True:
        next_add = input("Для добавления следующего продукта введите: да или entor, для вывода аналитики лубую клавишу\n")
        if next_add.lower() in ("да"):
            next_enter = next_add.lower() == "да"
            break
        else:
            print(f"Аналитика о товарах")
        for key, value in analytic_list.items():
            print(f"{key}: {value}")


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


