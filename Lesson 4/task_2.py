# 2.Написать два алгоритма нахождения i-го по счёту простого числа.
# ● Без использования Решета Эратосфена;
import cProfile
from math import isqrt


def without_algorithm_of_eratosthenes(num: int) -> list[int]:
    a = [2]
    for i in range(3, num + 1, 2):
        k = 0
        for j in a:
            if i % j == 0:
                k = 1
                break
        if k == 0:
            a.append(i)

    return a


print(cProfile.run("without_algorithm_of_eratosthenes(1000000)"))
print(len(without_algorithm_of_eratosthenes(1000000)))  # 78498

# cProfile test results for 1 million numbers:

#          78501 function calls in 264.248 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001  264.248  264.248 <string>:1(<module>)
#         1  264.176  264.176  264.247  264.247 task_2.py:7(without_algorithm_of_eratosthenes)
#         1    0.000    0.000  264.248  264.248 {built-in method builtins.exec}
#     78497    0.070    0.000    0.070    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# ● Использовать алгоритм решето Эратосфена
def with_algorithm_of_eratosthenes(n: int) -> list[int]:
    if n <= 2:
        return []
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, isqrt(n)):
        if is_prime[i]:
            for x in range(i*i, n, i):
                is_prime[x] = False

    return [i for i in range(n) if is_prime[i]]


print(cProfile.run("with_algorithm_of_eratosthenes(1000000)"))
print(len(with_algorithm_of_eratosthenes(1000000)))  # 78498

# cProfile test results for 1 million numbers:

#          6 function calls in 0.313 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.006    0.006    0.313    0.313 <string>:1(<module>)
#         1    0.193    0.193    0.307    0.307 task_2.py:27(with_algorithm_of_eratosthenes)
#         1    0.114    0.114    0.114    0.114 task_2.py:39(<listcomp>)
#         1    0.000    0.000    0.313    0.313 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method math.isqrt}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

