import string
import random

def random_string(n):
    str = ""
    for i in range(n):
        str += (random.choice(string.ascii_letters))
    return str

def counter(n):
    reg_lower = 0
    reg_upper = 0
    for i in n:
        if i in string.ascii_uppercase:
            reg_upper += 1
        elif i in string.ascii_lowercase:
            reg_lower += 1
    if reg_upper > reg_lower:
        return 1
    elif reg_lower > reg_upper:
        return -1
    else:
        return 0

def result(list):
    count_up = 0
    count_r = 0
    count_low = 0
    p_1 = ""
    p_2 = ""
    p_3 = ""
    for i in list:
        a = counter(i)
        if a == 1:
            count_up += 1
            p_1 = str(count_up * 100 / len(list)) + "%"
        elif a == -1:
            count_low += 1
            p_2 = str(count_low * 100 / len(list)) + "%"
        else:
            count_r += 1
            p_3 = str(count_r * 100 / len(list)) + "%"

    print('Процент строк, в которых больше заглавных букв: ', p_1)
    print('Процент строк, в которых больше строчных букв: ', p_2)
    print('Процент строк, в которых одинаковое число строчных и заглавных букв: ', p_3)


result([random_string(73), random_string(20), random_string(67), random_string(60), random_string(60), random_string(70),
        random_string(54), random_string(60), random_string(60), random_string(60), random_string(60), random_string(70),
        random_string(60), random_string(60), random_string(60), random_string(60)])