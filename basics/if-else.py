# Логические операторы
5 == 5 # True
4 == 5 # False
5 != 5 #False
5 != 2 # true
5 > 5 # False
5 < 5 # False
5 <= 5 # True

# Boolean Type
# true or false
bool(1) #true
bool(0) #false
bool(-24) #true
bool('hello') #true
bool('') #false
bool(' ') #True
bool(True) #true
bool(False) #false

# None
# тип данных с одним зна-ем None, котор исп для обознач пустых значений
bool(None) #false

a=None
bool(a) #false
a is None #True

# условные операторы
# нужны для того, чтобы создавать алгоритмы
a = int(input('Введите число: '))
if a > 0:
    print(f'Число {a} - положительное')
elif a < 0:
    print(f'Число {a} - отрицательное')
else:
    print(f'число {a} - 0')

# FizzBuzz
# Выведите числа от 1 до 100 (for i in range(1, 101):)
# если число кратно 3 вывести Fizz если кратно 5 - Buzz если число кратно 3 и 5 - FizzBuzz, ни 3 ни 5 - вывести число
for i in range(1, 201):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

# Тернарные операторы
# условия в одну строку
res = 'Hello' if a == 5 else 'Bye
print(res)
# Hello if a == 5
# Bye if a != 5