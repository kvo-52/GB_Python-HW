#Напишите программу, которая принимает на вход координаты точки 
#(X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
#в которой находится эта точка (или на какой оси она находится).


x = int(input('Введите число x≠0: '))
y = int(input('Введите число y≠0: '))

if x == 0 and y == 0:
    print('Ошибка!!! См. условие!)')
elif x > 0 and y > 0:
    print(f'Вы ввели координаты x = {x} и y = {y} => ваша точка находится в плоскости 1 ')
elif x < 0 and y > 0:
    print(f'Вы ввели координаты x = {x} и y = {y} => ваша точка находится в плоскости 2 ')
elif x < 0 and y < 0:
    print(f'Вы ввели координаты x = {x} и y = {y} => ваша точка находится в плоскости 3 ')
elif x > 0 and y < 0:
    print(f'Вы ввели координаты  x = {x} и y = {y} => ваша точка находится в плоскости 4 ')