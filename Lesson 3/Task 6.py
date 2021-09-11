# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и
# максимальным элементами. Сами минимальный и максимальный элементы в сумму не
# включать.
import random

massive = [random.randint(1, 100) for _ in range(0, 10)]
mx = 0
mn = float('inf')

for i in massive:
    if i < mn:
        mn = i
    if i > mx:
        mx = i

start = False
sum_of_elements = 0
print(massive)
print(mn, mx)


for i in massive:
    if (i == mn or i == mx) and not start:
        start = True
    elif (i == mn or i == mx) and start:
        break
    elif (i != mx or i != mn) and start:
        sum_of_elements += i

print(sum_of_elements)
