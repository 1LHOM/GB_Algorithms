# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности
# чисел. Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом
# с клавиатуры.

length = int(input('how many numbers to enter: '))
x = input('What number to count? : ')
number = ''

for i in range(length):
    number += input(f'enter {i+1} digit: ')

print(f'number {x} meets {number.count(x)} times in {number}')
