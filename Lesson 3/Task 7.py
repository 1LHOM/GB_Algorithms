# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть
# как равны между собой (оба являться минимальными), так и различаться.

import random

massive = [random.randint(1, 100) for _ in range(10)]
mn_1 = mn_2 = float('inf')
print(massive)
for x in massive:
    if x <= mn_1:
        mn_1, mn_2 = x, mn_1
    elif x < mn_2:
        mn_2 = x

print(mn_1, mn_2)

