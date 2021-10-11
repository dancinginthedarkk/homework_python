# y%4 == 0 високосный год
# d_30 = [4, 6, 9, 11] m in d_30
# d_31 = [1, 3, 5, 7, 8, 10, 12] m in d_31
def calc(d, m, y):
    '''
    Функция calc принимает следующие значения: день, месяц, год.
    И возвращает значение True или False в зависимости от соответствия критериям.
    '''
    d_30 = [4, 6, 9, 11]
    d_31 = [1, 3, 5, 7, 8, 10, 12]
    if (y <= 2021 and m <= 12 and d <= 31) and (m > 0 and d > 0 and y > 0):
        if (y < 2021) or (y == 2021 and m < 10) or (y == 2021 and m == 10 and d <= 9):
            if d <= 30 and m in d_30:
                return True
            elif d <= 31 and m in d_31:
                return True
            elif m == 2:
                if (d <= 28) or (y%4 == 0 and d == 29):
                    return True
    else:
        return False

d = int(input())
m = int(input())
y = int(input())

print(calc(d, m, y))