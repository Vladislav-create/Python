# 2.	Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

user_number = int(input('Введите число: '))

# делаю список с простыми числами до числа пользователя.
def get_prime_numbers(num):
    lst = []
    for i in range(2, num+1):
        for j in lst:
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst


print(get_prime_numbers(user_number), type(get_prime_numbers(user_number)))

result_arr = []
sub_result = user_number
for i in get_prime_numbers(user_number):
    while sub_result % i == 0:
        sub_result /= i
        result_arr.append(i)
print(result_arr)
