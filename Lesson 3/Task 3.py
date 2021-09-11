# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный
# элементы.
import random

massive = [random.randint(1, 100) for _ in range(0, 10)]
mx = 0
mn = float('inf')

for i in massive:
    if i < mn:
        mn = i
    if i > mx:
        mx = i

print(massive)

for idx, num in enumerate(massive):
    if num == mx:
        massive[idx] = mn
    elif num == mn:
        massive[idx] = mx

print(massive)
print(mn, mx)
