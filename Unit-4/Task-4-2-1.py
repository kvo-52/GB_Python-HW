# Задайте натуральное число N. Напишите программу, которая 
# составит список простых множителей числа N

number = int(input("Введите число: "))
i = 2  # первое простое число
my_list = []
simpleNumber = number
while i <= number:
    if number % i == 0:
        my_list.append(i)
        number //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {simpleNumber} приведены в списке: {my_list}")