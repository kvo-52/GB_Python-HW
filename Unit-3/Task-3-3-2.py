# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

def fract(number):
        return round(number%1,2)

list_num= [round(random.uniform(0,20),2)for i in range(random.randint(5,10))]
print(list_num)
list_num_fract=[]
for i in list_num:
        if i%1!=0:
            list_num_fract.append(fract(i))
print(list_num_fract)

max_num, min_num = list_num_fract[0], list_num_fract.pop(0)
for i in list_num_fract:
       if i>max_num:
              max_num=i
       elif i<min_num:
              min_num=i
print(max_num-min_num)                    