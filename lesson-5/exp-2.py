from random import randint

a = int(input('Введите количество конфет: '))
hod = 0
wins = {0: input("Введите имя игрока: "), 1: 'Бот'}
while a > 0:
    if a <= 28:
        print(f'Выиграл {wins[hod]}')
        break
    if hod == 0:
        print(f'Ход игрока {wins[hod]}')
        d = int(input('Введите количество конфет которое хотите взять: '))
        print(f'Осталось конфет: {a}')
        while not 1 <= d <= 28:
            d = int(input('Введите правильное количество конфет: от 1 до 28: '))
        a -= d
        print(f'Осталось конфет: {a}')
    else:
        print('Ход бота')
        d = a % 29
        if d == 0:
            d == randint(1, 28)
        a -= d
        print(f'Бот взял {d} конфет. Осталось конфет: {a}')
    hod = (hod+1) % 2
