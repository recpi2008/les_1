"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
 Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
def num_sum():
    try:
        with open('file5_5.txt', 'w+') as f_obj:
            line = input('Введите числа чисел разделенные пробелами \n')
            f_obj.writelines(line)
            num = line.split()

            print(sum(map(int, num)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Вы не коректно ввели числа')
num_sum()