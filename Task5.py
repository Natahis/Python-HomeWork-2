# Реализуйте алгоритм перемешивания списка.

import random


num = int(input('Введите размер списка: '))
num_list = list(range(num))
print(num_list)

for i in num_list:
    j = random.randint(0, i)
    num_list[i], num_list[j] = num_list[j], num_list[i]

print(num_list)
