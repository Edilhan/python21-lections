# Работа с файлами
# open - функ, кот открыв файл
# r - read только читает
# w - write только для записи, сначала все удаляет потом записывает
# a - append дозапись, все нвоое добав в конец
# x - создает файл, если он уже существ выдает ошибку
# rb - чтение в бинарном виде
# wb - запись в бинарном виде
# ab - дозапись

# Когда мы не указ режим - по умолчанию чтение
# open("test.txt") FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'
# open("test.txt", "w") # создает и записывает файл test.txt или открыл и почистил, а потом записал
# open("test.txt", "a") # обновляет файл или создает его если того не сущ
# res = file.read() - метод нельзя использ при режиме записи и дозаписи
# file.write() - запись в файл
# file.writelines([1,2,3]) - записывает без пробела в одну строку
# file.close() - обязательно закрываем

#  READ
file = open("test.txt")
res = file.read() # считывает весь файл
file.seek(0) # каретка переходит в индекс 0
print(file.read(5)) # выведет 5 символов
print(file.read(5)) # выведет след 5 симв
print(file.tell()) # показ текущ положение каретки
res = file.readlines() # возвращ список из линий из файла
file.close() 

file = open("test.txt", 'w+')
file.write("Hello world\nMakers\nBootcamp")
file.seek(0)
res = file.read()
file.seek(0)
file.write("New lines\n")
file.write(res)
file.close()



#  WITH
# with - позволяет в начале конструкции вызывает __enter__  а в конце вызывает __exit__
class Test: 
    def __enter__(self):
        print("начало работы")
        return self

    def __exit__(self):
        print("Конец работы ")

    def hello(self):
        print("Hello World")

with Test() as test:
    test.hello()


