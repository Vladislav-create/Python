#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

print('Введите цифру, обозначающую день недели')
day = int(input())
if day == 6 or day == 7:
    print('Это выходной день')
elif day < 1 or day > 7:
    print('Введите число в диапазоне от 1 до 7')
else:
    print('Это будний день')