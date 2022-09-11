# Реализуйте алгоритм перемешивания списка.


from random import randint, random

ls = [10, 11, 12, 13, 14, 15]
ls_random_index = []
ls_new = []
print(ls)
while len(ls_random_index) < len(ls):
    random_number = randint(0, len(ls)-1)
    if ls_random_index.count(random_number) == 0:
        ls_random_index.append(random_number)
for i in ls_random_index:
    ls_new.append(ls[i])
print(ls_new)
ls = ls_new
print(ls)
