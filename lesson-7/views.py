


def user_menu():
    menu = ['Показать всех сотрудников', 'Добаыить сотрудника',
            'Удалить сотрудника', 'Изменить данные сотрудника']
    for item in enumerate(menu, 1):
        print(*item)
    num = int(input('Выберите пункт меню: '))
    return num

def user_data_entry():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    phone = input('Введите номер телефона: ')  
    data_new_user=[name, surname, phone]
    return data_new_user

def views_show_users(users):
    for item in enumerate(users, 1):
        print(*item)

def user_num_for_delete():
    return int(input('Введите номер записи для удаления: '))
     

def user_num_for_update():
    return int(input('Введите номер записи для редактирования: '))-1