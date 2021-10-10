import random
def random_name(names, surnames, sec_names, num):
    i = 0
    while i < num:
        yield (random.choice(names) + ' ' + random.choice(surnames) + ' ' + random.choice(sec_names))
        i+=1
first = ['Сергей', 'Дмитрий', 'Иван', 'Олег', 'Петр']
second = ['Иванов', 'Сидоров', 'Петров', 'Никитин', 'Смирнов']
third = ['Олегович', 'Владимирович', 'Дмитриевич', 'Иванович', 'Сергеевич']
for i in random_name(first,second,third,3):
    print(i)