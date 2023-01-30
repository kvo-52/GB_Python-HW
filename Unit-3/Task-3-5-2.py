# Задайте число. Составьте список чисел Фибоначчи, в том числе для 
# отрицательных индексов.

def positiv_fib(n):
    positiv_list=[0,1]
    for i in range (n-1):
        positiv_list.append(positiv_list[-2]+positiv_list[-1])
    return positiv_list
    
def negativ_fib(n):
    negativ_list=[0,1]
    for i in range (n-1):
        negativ_list.append(negativ_list[-2]-negativ_list[-1])
    return negativ_list
    
print(negativ_fib(8)[::-1]+positiv_fib(8)[1:])