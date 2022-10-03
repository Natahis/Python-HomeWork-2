# Задайте список из n чисел последовательности 
# $(1+1/n)^n и выведите на экран их сумму.

# Пример:
# - Для n = 6: [2, 2, 2, 2, 2, 3] -> 13


import numbers


number = int(input('Введите положительное целое число n: '))
result = []
for i in range(1, number+1):
    # sum = sum + (1+1/i)**i
    result.append(round((1+1/i)**i))
print(f'Для числа {number}: {result} -> {sum(result)}')