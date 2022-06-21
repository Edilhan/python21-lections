from random import Random, random, randrange
# from turtle import end_fill
# import random

a = input('Как зовут')
b = input('Готов? (yes/no) ')
while b == 'yes':
    c = randrange(1,10)
    print(c)
    d = int(input('Введи число '))
    i = int()
    while c != d:
        i = i + 1
        d = int(input('Введи число '))
    else:
        print('Кол-во попыток', i)
        b = input('Готов? (yes/no) ')
        if b == 'no':
            print('Игра завершена')
            break
if b == 'no':
    print('Игра завершена')
else:
    print('введи yes или no')