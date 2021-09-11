# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и
# позицию (индекс) в массиве.
import random

massive = [random.randint(-200, 0) for _ in range(10)]
print(massive)
mx = float('-inf')
for i in massive:
    if i > mx:
        mx = i

for idx, num in enumerate(massive):
    if num == mx:
        print(f'{num} is biggest negative number in the list\n'
              f'index = {idx}')
