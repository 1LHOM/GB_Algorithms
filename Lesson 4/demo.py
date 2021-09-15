import cProfile
import timeit


def get_count(items):
    return len(items)


def get_sum(items):
    sum_ = 0
    for i in items:
        sum_ += i
    return sum_


def second_smallest(numbers):
    m1 = m2 = float('inf')
    print(m1, m2)
    for x in numbers:
        if x <= m1:
            m1, m2 = x, m1
        elif x < m2:
            m2 = x
    return m1, m2


def main():
    a = [3, 5, 6, 7]
    s = get_count(a)
    t = get_sum(a)
    w = second_smallest(a)


cProfile.run('main()')
# print(timeit.timeit('second_smallest([52, 72, 67, 65, 85, 99, 85, 59, 72, 95])'))
print(second_smallest([52, 72, 67, 65, 85, 99, 85, 59, 72, 95]))
print(timeit.timeit('x = main()'))
