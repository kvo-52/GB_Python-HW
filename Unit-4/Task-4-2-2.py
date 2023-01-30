# Задайте натуральное число N. Напишите программу, которая 
# составит список простых множителей числа N

def primfactors(number):
   i = 2
   primfactors = []
   while i * i <= number:
       while number % i == 0:
           primfactors.append(i)
           number = number / i
       i = i + 1
   if number > 1:
       primfactors.append(number)
   return primfactors

number = int(input("Введите число: "))
my_list = primfactors(number)
print(my_list)
