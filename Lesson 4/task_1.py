# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в
# рамках практического задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
import cProfile

# task example:  Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
from functools import reduce


def test_sum_1(num):
    s = sum(map(int, num))
    p = reduce((lambda x, y: x * y), list(map(int, num)))
    return s, p

# ----- timeit test results -----

# test_sum_1('55555')
# 1000 loops, best of 5: 4.66 usec per loop

# test_sum_1('5555555555')
# 1000 loops, best of 5: 7.39 usec per loop

# test_sum_1('555555555555555')
# 1000 loops, best of 5: 10.4 usec per loop

# test_sum_1('555555555555555555555555555555')
# 1000 loops, best of 5: 19.4 usec per loop


print(cProfile.run("test_sum_1('5555555555')"))

# ----- cProfile results -----
#
#    15 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_2.py:10(test_sum_1)
#         9    0.000    0.000    0.000    0.000 task_2.py:12(<lambda>)
#         1    0.000    0.000    0.000    0.000 {built-in method _functools.reduce}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


def test_sum_2(number):
    s = 0
    p = 1
    for i in number:
        s += int(i)
        p *= int(i)
    return s, p

# ----- timeit test results -----

# test_sum_2('55555')
# 1000 loops, best of 5: 3.27 usec per loop

# test_sum_2('5555555555')
# 1000 loops, best of 5: 5.92 usec per loop

# test_sum_2('555555555555555')
# 1000 loops, best of 5: 8.5 usec per loop

# test_sum_2('555555555555555555555555555555')
# 1000 loops, best of 5: 17.4 usec per loop


print(cProfile.run("test_sum_2('5555555555')"))

#    ----- cProfile results -----
#
#    4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_2.py:35(test_sum_2)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

