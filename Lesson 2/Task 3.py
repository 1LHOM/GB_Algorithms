# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на
# экран. Например, если введено число 3486, то надо вывести число 6843.

# version 1.0
number = input('Enter any number or symbol: ')
rv_num = ''

for i in reversed(number):
    rv_num += i

print(rv_num)

# version 2.0
print(*reversed(input('Enter anything to reverse: ')), sep='')
