"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое
число представляется как коллекция, элементы которой это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из модуля
collections (пусть это и не очевидно с первого раза. Вы же не Голландец ;-).
"""


def hex_to_decimal(hex_: list) -> int:
    alpha_dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    decimal_num = 0
    prev = 1

    for idx, i in enumerate(hex_[::-1]):
        if i.isdigit():
            if idx == 0:
                decimal_num += int(i)
            else:
                decimal_num += int(i) * (16 * prev)
                prev *= 16
        elif i in alpha_dict:
            if idx == 0:
                decimal_num += alpha_dict[i]
            else:
                decimal_num += alpha_dict[i] * (16 * prev)
                prev *= 16
        else:
            raise ValueError
    return decimal_num


def decimal_to_hex(num: int) -> list:
    if num < 0:
        raise ValueError
    hex_dict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    hex_list = []
    a = 16
    while num != 0:
        if num < a:
            division = num // (a / 16)
            if division < 10:
                hex_list.append(str(int(division)))
            else:
                hex_list.append(hex_dict[int(division)])
            if num < 16:
                num = 0
            else:
                num = num % (a / 16)
                if num == 0:
                    hex_list.append(str(int(num)))
            a = a / 16
        else:
            a *= 16

    return hex_list


def hex_calculator(num_1: list, num_2: list) -> list:
    num_1 = hex_to_decimal(num_1)
    num_2 = hex_to_decimal(num_2)
    result = []
    addition = num_1 + num_2
    multiplication = num_1 * num_2
    result.append(decimal_to_hex(addition))
    result.append(decimal_to_hex(multiplication))
    return result


x = [i for i in input('Enter first hex number: ').upper()]
y = [i for i in input('Enter second hex number: ').upper()]

print(hex_calculator(x, y))
