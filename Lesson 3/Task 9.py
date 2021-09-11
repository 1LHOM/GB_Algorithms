# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

massive = [[7], [23, 45, 83, 1, 31], [34, 51, 10, 34], [12, 4, 56, 3], [54, 23, 45]]
min_list = 0
min_len = float('inf')

for i in massive:
    if len(i) < min_len:
        min_len = len(i)
        min_list = i

max_num = 0
for i in min_list:
    if i > max_num:
        max_num = i

print(max_num)
