# Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (значения от 0 до 100) многочлена и записать
# в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


import random

def write_file(st):
    with open('file_4_4.txt', 'w') as data:
        data.write(st)

def rnd():
    return random.randint(0, 101)

def create_factors(k):
    lst = [rnd() for i in range(k+1)]
    return lst

def create_str(sp):
    lst = sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr


k= int(input("Введите натурильную степень k: "))
koeff = create_factors(k)
write_file(create_str(koeff))



# import random
# k = int(input())
# result = ""
# for i in range(k,-1,-1):
#     koeff = random.randint(0,3)
#     if koeff == 0:
#         continue
#     if koeff == 1:
#         if i == 1:
#             result += f"x+"
#         elif i == 0:
#             result += f"{koeff}"
#         else:
#             result += f"x**{i}+"
#     else:
#         if i == 1:
#             result += f"{koeff}*x+"
#         elif i == 0:
#             result += f"{koeff}"
#         else:
#             result += f"{koeff}*x**{i}+"
# result += " = 0"
# print(result)
#
# f = open("filepol.txt","w")
# f.write(result)
# f.close()

