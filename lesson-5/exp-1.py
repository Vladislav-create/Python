stroka = input().split()
res = list(filter(lambda s: 'абв' not in s, stroka))
print(res)