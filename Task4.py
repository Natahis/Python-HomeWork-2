# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

num = int(input('Введите целое число: '))
if num < 0: num = - num
num_list = list(range(-num,num+1))
path = 'file.txt'
data = open(path, 'r')
mult = 1
for i in data:
    mult *= num_list[int(i)-1]
data.close()
print(num_list)
print(f'Произведение элементов на указанных позициях = {mult}')