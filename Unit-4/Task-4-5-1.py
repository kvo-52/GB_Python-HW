# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

with open('file-5_1.txt', 'w', encoding='utf-8') as file:
    file.write('4*x^2 + 5*x^3')
with open('file-5-2.txt', 'w', encoding='utf-8') as file:
    file.write('2*x^4 + 7*x^2')

with open('file-5_1.txt','r') as file:
    file_1 = file.readline()
    list_of_file_1 = file_1.split()


with open('file-5-2.txt','r') as file:
    file_2 = file.readline()
    list_of_file_2 = file_2.split()

print(f'{list_of_file_1} + {list_of_file_2}')
sum_poly = list_of_file_1 + list_of_file_2

with open('sum_file-5.txt', 'w', encoding='utf-8') as file:
    file.write(f'{list_of_file_1} + {list_of_file_2}')

