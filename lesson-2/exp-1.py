# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

result = 0
num = input('Введите вещественное число: ')
arr = []
for i in num:
    if i != ',':
        arr.append(i)
print(arr)
for k in arr:
    result = result + float(k)

print(f'Сумма цифр = {int(result)}')
