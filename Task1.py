# Напишите программу, которая принимает на вход вещественное число и 
# показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11


from tkinter import N


number = float(input('Введите любое вещественное число: '))
if number < 0: number = number * (-1)
sum = 0
for i in str(number):
        if i != '.':
            sum += int(i)

print(F'{number} -> {sum}')