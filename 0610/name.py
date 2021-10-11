def f():

    slowar = {}
    name = ''
    num = ''

    while name != 'q' and num != 'q':
        name = input()
        if name == 'q':
            break
        num = input()
        if num == 'q':
            break
        if num[0] == '+' and num[1].isdigit \
            and num[2] == "-" and num[3:6].isdigit \
            and num[6] == '-' and num[7:10].isdigit \
            and num[10] == '-' and num[11:13].isdigit \
            and num[13] == '-' and num[14:] and len(num) == 16:
            slowar[name] = num
        else:
            print('Wrong!')
    print(slowar)

f()