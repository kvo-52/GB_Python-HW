# Задача 32:  Напишите программу, которая на вход принимает два числа A и B,
#  и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def pow_two_numb(a,b,rezult):
    if b==1:
        return rezult
    return pow_two_numb(a,b-1, rezult*a)
    

a=int(input())
b=int(input())
rezult=a

print(pow_two_numb(a,b,rezult))