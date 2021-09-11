# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа
# должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю
# ячейку строки. В конце следует вывести полученную матрицу.

massive = []
for i in range(4):
    massive.append([int(input('Enter number: ')) for _ in range(4)])
    print(f'end of {i+1} line')

print(massive)
sum_of_line = 0

for i in massive:
    for j in i:
        sum_of_line += j
    i.append(sum_of_line)
    print(i)


