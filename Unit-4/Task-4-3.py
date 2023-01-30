# Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности.

from random import randint

number = int(input('Введите размер списка '))
list1 = []

for i in range(number):
    list1.append(randint(0, 9))

print(f"Исходный список: {list1}")
new_list = []
[new_list.append(i) for i in list1 if i not in new_list]
print(f"Список неповторяющихся элементов: {new_list}") 