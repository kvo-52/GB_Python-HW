# Напишите программу, которая будет преобразовывать десятичное число
# в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input('Введите число: '))
number2 = ''
while number > 0:
    number2 = str(number%2) + number2
    number = number // 2
print(number2)
