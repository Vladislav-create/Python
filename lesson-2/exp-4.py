# Задайте числами список из N элементов, заполненных из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

num = int(input('Введите число n: '))
ls = list(range(-num, num+1))
print(ls)

arr_position = []
path = 'file.txt'
data = open(path, 'r')
for line in data:
    arr_position.append(int(line))
data.close()
print(arr_position)
print(ls[arr_position[0]]*ls[arr_position[1]])