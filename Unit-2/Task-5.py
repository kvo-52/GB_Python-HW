#Реализовать алгоритм перемешивания списка.

import random
my_list = [random.randint(0,5) for i in range(random.randint(5,10))]
print(f"исходный список:\n {my_list}")
random.shuffle(my_list)
print(f"список после перемешивания:\n{my_list}")