a = {'mango':500,'banana':250,'pineapple':655}
try:
  i = 'mango'
  print(a.get(i))
except:
  print('Такого ключа нет')