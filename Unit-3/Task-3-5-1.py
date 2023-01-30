# Задайте число. Составьте список чисел Фибоначчи, в том числе для 
# отрицательных индексов.


fibonache = int(input('Задайте число: '))
my_list = []
for i in range(fibonache+1):
    if i==0:
        my_list.append(i)
    elif i==1:
        my_list.append(i)
        my_list.insert(0, i)
    else:
        my_list.append(my_list[len(my_list)-1]+my_list[len(my_list)-2])
        my_list.insert(0, (-1)**(i-1)*my_list[len(my_list)-1])
print(my_list)