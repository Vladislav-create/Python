
lst = [2, 3, 4, 5, 6]

def func(ls):
    sqrt=[]
    for i in range(len(ls)+1//2):
        sqrt.append(ls[i]*ls[len(ls)-1-i])
    return sqrt
print(func(lst))
