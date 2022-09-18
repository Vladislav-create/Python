ls = [i for i in range(1, 20, 2)]
print(ls)
result_arr = []
for i in ls:
    if ls.index(i, 0, len(ls)) % 2 != 0:
        result_arr.append(i)
    print(ls.index(i, 0, len(ls)))
sum = 0
for i in result_arr:
    sum += i
print(result_arr)
print(sum)
