import csv
import views

PATH_FILE = 'Журнал сотрудников.csv'


def create_user(user_data):
    with open(PATH_FILE, 'a', encoding='UTF8') as file:
        file_writer = csv.writer(file, delimiter=';', lineterminator='\r')
        file_writer.writerow(user_data)

def show_users():
    lst = []
    with open(PATH_FILE, 'r', encoding='UTF8') as file:
        file_reader = csv.reader(file, delimiter=';', lineterminator='\r')
        for item in file_reader:
            lst.append(item)
    return lst

def delete_user(user_select):
    lst = show_users()
    del lst[user_select-1]
    with open(PATH_FILE, 'w', encoding='UTF8') as file:
        file_writer = csv.writer(file, delimiter=';', lineterminator='\r')
        for item in lst:
            file_writer.writerow(item)

def apdate_user(user_select, lst):
    lst[user_select] = views.user_data_entry()
    with open(PATH_FILE, 'w', encoding='UTF8') as file:
        file_writer = csv.writer(file, delimiter=';', lineterminator='\r')
        for item in lst:
            file_writer.writerow(item)
