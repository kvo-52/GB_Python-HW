#Напишите программу, которая принимает на вход вещественное число и 
#показывает сумму его цифр.
#Пример:
#- 6782 -> 23
#- 0,56 -> 11


x = input('Введите число: ')
my_list=str(x)
my_list = my_list.replace('.', '')
my_list = my_list.replace(',', '')
list_str=list(my_list)
list_number=map(int, list_str)
sumNumber= sum(list_number)

print(sumNumber)