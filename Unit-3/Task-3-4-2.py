# Напишите программу, которая будет преобразовывать десятичное число
# в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


# спомощью функции через рекурсию
def dec_to_bin(num, rezult=''):
    if num==0:
        return rezult[::-1]
    rezult+=str(num%2)
    return dec_to_bin(num//2, rezult)

n=int(input('Введите число: '))
# print(bin(n)[2:])  # аналогично всему написанному
print(dec_to_bin(n)) 