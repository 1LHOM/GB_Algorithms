# 1.  Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не
# должна завершаться, а должна запрашивать новые данные для вычислений. Завершение
# программы должно выполняться при вводе символа '0' в качестве знака операции. Если
# пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об
# ошибке и снова запрашивать знак операции. Также сообщать пользователю о невозможности
# деления на ноль, если он ввел 0 в качестве делителя.

symbol = ''
while symbol != '0':
    try:
        first_num = int(input('enter first number: '))
        while symbol not in ['+', '-', '*', '/', '0']:
            symbol = input('enter one of these symbols: +, -, *, /, 0 \n')
            if symbol not in ['+', '-', '*', '/']:
                print(f'{ValueError} invalid symbol or unsupported operator, please try again!')
        second_number = int(input('enter second number: '))
        if symbol == '+':
            print(f'{first_num} + {second_number} = {first_num + second_number}')
        elif symbol == '-':
            print(f'{first_num} - {second_number} = {first_num - second_number}')
        elif symbol == '*':
            print(f'{first_num} * {second_number} = {first_num * second_number}')
        elif symbol == '/':
            print(f'{first_num} / {second_number} = {first_num / second_number}')

    except ZeroDivisionError:
        print(f'{ZeroDivisionError}: Number can not be divided by zero!')
    except ValueError:
        print(f'{ValueError} Detected unsupported value!')

print(f'Process has been finished!')
