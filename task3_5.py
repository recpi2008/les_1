"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже
подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
к полученной ранее сумме и после этого завершить программу.
"""
user_nums = input("Введите строку чисел, разделенных пробелом: ")
def my_func (user_nums):
    d = 0
    for idx, nums in enumerate(user_nums.split(" ")):
        a = int(nums)
        d = d + a
    return d
res_sum = my_func (user_nums)
print(res_sum)
o_res = 0 + res_sum
while True:
    next_add = input("Для добавления следующих чисел нажмите 'ENTER', для завершения введите '@': ")
    if next_add.lower() in ("ENTER"):
        next_enter = next_add.lower() == "ENTER"
        user_nums = input("Введите следующие числа:")
        sec_res = my_func(user_nums)
        o_res = o_res + sec_res
        print(o_res)
    elif next_add.lower() in ("@"):
        print("Программа завершeна")
        break
    else:
        break
print(f"Ваш итоговый результат: {o_res}")
