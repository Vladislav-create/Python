# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

arr = []
number = input('Введите число: ')
lst = list(range(1, int(number) + 1))
for i in lst:
    renderList = list(range(1, i+1))
    res = 1
    for k in renderList:
        res = res * k
    arr.append(res)
print(arr)
