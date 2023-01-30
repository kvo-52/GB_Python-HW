# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint

list_num=[randint (1,20) for i in range (randint(5,10))]
print(list_num)
multi=[]
lenght=len(list_num)
middile= lenght//2+lenght%2
for i in range (middile):
    multi.append(list_num[i]*list_num[lenght-i-1])
print (multi)