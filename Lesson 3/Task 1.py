# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из
# чисел в диапазоне от 2 до 9.

num_list = [2, 3, 4, 5, 6, 7, 8, 9]
my_dict = {}

for i in num_list:
    for j in range(2, 100):
        if j % i == 0:
            if i not in my_dict:
                my_dict[i] = 1
            else:
                my_dict[i] += 1

print(my_dict)
