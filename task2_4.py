"""
Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово
 с новой строки. Строки необходимо пронумеровать. Если в слово длинное, выводить только первые
 10 букв в слове.
"""
user_str = input("Введите несколько слов разделённых пробелами")
user_word = []
a = 1
for el in range(user_str.count(' ') + 1):
    user_word = user_str.split()
    if len(str(user_word)) <= 10:
        print(f" {a} {user_word [el]}")
        a += 1
    else:
        print(f" {a} {user_word [el] [0:10]}")
        a += 1
#fast decision from teacher
"""
user_word = input()

for idx, word in enumerate(user_word.split(" ")):
    print(f"{idx}:{word[:10]}")
"""
