def f():

    slowar = {}
    name = ''
    num = ''

    while name != 'q' and num != 'q':
        name = input('name: ')
        if name == 'q':
            break
        num = input('num: ')
        if num == 'q':
            break
        if len(num) == 16:
            num[0] == '+' and num[1].isdigit \
            and num[2] == "-" and num[3:6].isdigit \
            and num[6] == '-' and num[7:10].isdigit \
            and num[10] == '-' and num[11:13].isdigit \
            and num[13] == '-' and num[14:]
            slowar[name] = num
        else:
            print('Wrong!')
    print(slowar)

f()