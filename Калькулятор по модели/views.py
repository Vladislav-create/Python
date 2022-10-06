def show_menu():
    puncts = {
        1: 'Калькулятор',
        2: 'Перевод величин',
        3: 'Что либо еще'
    }
    print('\nВыберите пункт меню:\n')
    for num,item in puncts.items():
        print(f'{num}: {item}\n')
    while True:
        try:
            result=int(input())
            if result not in puncts:
                raise ValueError
            return result
        except ValueError:
            print('Введите число от 1 до 3')

def calc():
    return input('\nВведите выражение для его рассчета\n')

def converter_view():
    return int(input('\nВведите колличество кг: \n'))

def output(result):
    if result == 'Error':
        print('Ошибка, проверьте введенное выражение')
    else:
        print(f'\nРезультат вычислений: {result}\n')

def output_converter(result):
    print(f'\nРезультат: {result} грамм\n')    