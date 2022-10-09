from unittest import result


def user_menu():
    menu = ['Показать всех сотрудников', 'Добаыить сотрудника',
            'Удалить сотрудника', 'Изменить данные сотрудника']
    for item in enumerate(menu, 1):
        print(*item)
    num = int(input('Выберите пункт меню: '))
    return num


def show_all_users(data):
    for item in data:
        print(item)


def add_user():
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    phone = input('Введите телефон: ')
    description = input('Введите должность: ')
    arr = [surname, name, phone, description]
    return arr


def del_user():
    num = int(input('Введите id сотрудника, которого хотите удалить: '))
    return num

def update_user():
    id = int(input('Введите id сотрудника, по которому хотите изменить данные: '))
    what_change= input('Что меняем?(surname, name, phone, description): ')
    new_value = input('Введите новое значение: ')
    result = [id, what_change, new_value]
    return result