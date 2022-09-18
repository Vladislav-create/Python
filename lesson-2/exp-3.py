# Задайте список из n чисел последовательности (1+1/n)**n выведите на экран их сумму.

n = int(input('Введите число n: '))
result_arr = []
result_sum = 0
for i in range(1, n+1):
    el = round((1+1/i)**i, 2)
    result_arr.append(el)
print(result_arr)
for i in result_arr:
    result_sum += i
print(round(result_sum, 2))
