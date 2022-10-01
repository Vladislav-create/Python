data = open('./входные данные.txt', 'r')
for line in data:
    print(f'\nСтрока из документа: \n {list(line)} \n')
data.close()
print(f'Длина строки: {len(line)} \n')

result = ''
k=1
for i in range(len(line)-1):
    if line[i] == line[i+1]:
        k+=1
    else:
        result = result + f'{k}{line[i]}'
        k=1
result = result + f'{k}{line[i]}'
result_data = open('./Результат кодирования.txt', 'w')
result_data.writelines(''.join(result+'\n'))
result_data.close()
    
print(f'Результат кодирования: {result}\n')

