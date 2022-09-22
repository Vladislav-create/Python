# 4.	Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# o	k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint



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

def polinome(k, file_name):
    factors = [randint(1,101) for _ in range(0,k+1)]
    res = create_formula(factors)
    with open(file_name,'w', encoding='utf-8') as f:
        f.write(' '.join([str(i) for i in factors[::-1]])+'\n')
        f.write(res)
polinome(3, 'file_1.txt')
polinome(3, 'file_2.txt')
