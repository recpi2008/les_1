"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться
в новый текстовый файл.
"""
nun_rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('file_task5_4.txt', 'r', encoding="UTF-8") as f_obj:
    for el in f_obj:
        el = el.split(' ', 1)
        new_file.append(nun_rus[el[0]] + '  ' + el[1])
    print(new_file)

with open('file_4_new.txt', 'w', encoding="UTF-8") as f_obj_new:
    f_obj_new.writelines(new_file)
