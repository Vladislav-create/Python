def create_formula(factors):
    k=len(factors)
    res=''
    for i in range(0, len(factors)):
        if i == len(factors)-1:
            res+=f'{factors[i]}'
        elif k==1:
            res+=f'{factors[i]}x + '
        else:
            res += f'{factors[i]}x^{k} + '
        k -=1
    return res

pol_1=[]
with open('file_1.txt') as f1, open('file_2.txt') as f2:
    factors1=[int(i) for i in f1.readline().split()]
    factors2=[int(i) for i in f2.readline().split()]
if len(factors2)==len(factors1):
    res=[a+b for a, b in zip(factors1,factors2)]
elif len(factors1)>len(factors2):
    res = factors1.copy()
    for i in range(len(factors2)):
        res[i]+=factors2[i]
else:
    res = factors2.copy()
    for i in range(len(factors1)):
        res[i]+=factors1[i]
with open('file_3.txt', 'w') as f:
    f.write(create_formula(res[::-1]))
