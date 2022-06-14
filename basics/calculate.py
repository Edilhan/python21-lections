a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
c = input('Выберите операцию из следующих +-*/%**// : ')
res = None
if c == '+':
    res = a + b
    print(res)
elif c == '-':
    res = a - b
    print(res)
elif c == '*':
    res = a * b
    print(res)
elif c == '/':
    res = a / b
    print(res)
elif c == '%':
    res = a % b
    print(res)
elif c == '**':
    res = a ** b
    print(res)
elif c == '//':
    res = a // b
    print(res)
else:
    print('Данной операции нет в системе')