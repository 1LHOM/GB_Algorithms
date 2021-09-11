# 4. Определить, какое число в массиве встречается чаще всего.
import random

massive = [random.randint(1, 11) for _ in range(20)]
print(massive)
my_dict = {}

for i in massive:
    if i not in my_dict:
        my_dict[i] = 1
    else:
        my_dict[i] += 1

max_repeat = 0
for i in my_dict.values():
    if i > max_repeat:
        max_repeat = i

print(max_repeat)

for k, v in my_dict.items():
    if max_repeat == v:
        print(f'number {k} repeats: {v} times')
