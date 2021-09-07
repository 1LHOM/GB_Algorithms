# 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если
# введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

number = input('Enter number: ')
odd_num = []
even_num = []

for i in number:
    if int(i) % 2 == 0:
        even_num.append(int(i))
    else:
        odd_num.append(int(i))

print(f'There is(are) {len(even_num)} even number(s) {even_num}\n'
      f'There is(are) {len(odd_num)} odd number(s) {odd_num}')
