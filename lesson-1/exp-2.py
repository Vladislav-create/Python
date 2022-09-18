# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# t = 3
# ls = ["{0:b}".format(i).zfill(t) for i in range(0, 1 << t)]  # нашел в интернете
# print(ls)

# for i in ls:

#     x = int(i[0])
#     y = int(i[1])
#     z = int(i[2])

#     print('x =', x, 'y =', y, 'z =', z)
#     print(not (x or y or z) == ((not x) and (not y) and (not z)))

def predicat(x, y, z):
    return not (x or y or z) == ((not x) and (not y) and (not z))


for x in range(2):
    for y in range(2):
        for z in range(2):
            print(predicat(x, y, z))
