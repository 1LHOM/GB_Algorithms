# 6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его
# отгадать не более чем за 10 попыток. После каждой неудачной попытки должно сообщаться
# больше или меньше введенное пользователем число, чем то, что загадано. Если за 10
# попыток число не отгадано, то вывести загаданное число.
from random import randint

rand_num = randint(0, 100)
chance = 10
print('Welcome to the game!')

while chance != 0:
    x = int(input('Enter any number between 0-100: '))
    if x == rand_num:
        print(f'Congratulations secret number is {rand_num}!')
        break
    else:
        if x > rand_num:
            print('your number is big ')
        else:
            print('your number is small ')
    chance -= 1
else:
    print('Game is Over!')
