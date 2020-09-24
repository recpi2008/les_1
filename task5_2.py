"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества
 строк, количества слов в каждой строке.
"""
my_file = open('text_task5_2.txt', 'r', encoding="UTF-8")
content = my_file.read()
print(content)
my_file = open('text_task5_2.txt', 'r', encoding="UTF-8")
content = my_file.readlines()
print(f'Количество строк в файле - {len(content)}')

my_file = open('text_task5_2.txt', 'r',  encoding="UTF-8")
content = my_file.read()
content = content.split()
print(f'Количество слов - {len(content)}')
my_file.close()