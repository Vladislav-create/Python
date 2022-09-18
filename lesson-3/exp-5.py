# def fib(n):
#     if n in [1, 2, -1]:
#         return 1
#     else:
#         return fib(n+2)-fib(n+1)


# list = []
# for i in range(-10, 0):
#     list.append(fib(i))
# print(list)

n =8
fib = [0,1]
for i in range(2,n+1):
    fib.append(fib[-1]+fib[-2])
for i in range(n):
    fib = [fib[1]-fib[0]]+fib
print(fib)