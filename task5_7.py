"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь
со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json
firm_profit = {}
average_dict = {}
tmb = 0
average_profit = 0
i = 0
with open('file_task5_7.txt', 'r', encoding='UTF-8') as f_obj:
    for line in f_obj:
        name, firm, earning, damage = line.split()
        firm_profit[name] = int(earning) - int(damage)
        if firm_profit.setdefault(name) >= 0:
            tmb = tmb + firm_profit.setdefault(name)
            i += 1
    if i != 0:
        average_profit = tmb / i
        print(f'Прибыль средняя - {average_profit}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    average_dict = {'средняя прибыль': round(average_profit)}
    firm_profit.update(average_dict)
    print(f'Прибыль каждой компании - {firm_profit}')

with open('file_7.json', 'w') as write_js:
    json.dump(firm_profit, write_js)

    js_str = json.dumps(firm_profit)
    print(f'Итоговый список в виде json-объекта: \n '
          f' {js_str}')