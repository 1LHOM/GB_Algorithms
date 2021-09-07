# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.
from random import randrange

my_list = [str(randrange(100, 10000)) for _ in range(10)]

my_dict = {}
for i in my_list:
    s = 0
    for j in i:
        s += int(j)
    my_dict[i] = s

print(my_list)
max_sum = max(my_dict.values())
for k, v in my_dict.items():
    if v == max_sum:
        print(f'biggest number {k}\nsum of digits = {v}')
