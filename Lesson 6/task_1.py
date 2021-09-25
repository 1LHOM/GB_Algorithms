import sys
"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных
программах в рамках первых трех уроков. Проанализировать результат и определить
программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для
одной и той же задачи. Результаты анализа вставьте в виде комментариев к коду. Также укажите в
комментариях версию Python и разрядность вашей ОС.
"""

"""
Common object sizes for Python 3.x
Empty
Bytes  type        scaling notes
28     int         +4 bytes about every 30 powers of 2
37     bytes       +1 byte per additional byte
49     str         +1-4 per additional character (depending on max width)
48     tuple       +8 per additional item
64     list        +8 for each additional
224    set         5th increases to 736; 21nd, 2272; 85th, 8416; 341, 32992
240    dict        6th increases to 368; 22nd, 1184; 43rd, 2280; 86th, 4704; 171st, 9320
136    func def    does not include default args and other attrs
1056   class def   no slots 
56     class inst  has a __dict__ attr, same scaling as dict above
888    class def   with slots
16     __slots__   seems to store in mutable tuple-like structure
                   first slot grows to 48, and so on.
"""


# creating function to calculate size of the objects
def get_obj_size(obj):
    size = sys.getsizeof(obj)
    if isinstance(obj, (list, tuple, set, frozenset)):
        return size + sum(map(get_obj_size, obj))
    elif isinstance(obj, dict):
        return size + sum(map(get_obj_size, obj.keys())) + sum(map(get_obj_size, obj.values()))
    else:
        return size


""" example 1
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из
# # чисел в диапазоне от 2 до 9.
"""
sum_1 = 0

num_list = [2, 3, 4, 5, 6, 7, 8, 9]
sum_1 += get_obj_size(num_list)

num_dict = {}  # size of num_dict will be added to sum when it's filled

for i in num_list:
    for j in range(2, 100):
        if j % i == 0:
            if i not in num_dict:
                num_dict[i] = 1
            else:
                num_dict[i] += 1

sum_1 += get_obj_size(range)
for i in range(2, 100):  # calculating the numbers are in range of 2-100 and the range object too
    sum_1 += get_obj_size(i)

sum_1 += get_obj_size(num_dict)
sum_1 += get_obj_size(print)  # adding size of print object
print(sum_1)  # 4376

""" example 2
Во втором массиве сохранить индексы четных элементов первого массива. Например, если
дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1,
4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого
массива стоят четные числа.
"""
sum_2 = 0
massive = [8, 3, 15, 6, 4, 2]
sum_2 += get_obj_size(massive)

massive_2 = []

for idx, num in enumerate(massive):
    sum_2 += get_obj_size(idx)
    sum_2 += get_obj_size(num)
    if num % 2 == 0:
        massive_2.append(idx)

sum_2 += get_obj_size(enumerate)

print(sum_2)  # 1060

# System information
# Version: 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)]
# Platform: win32
