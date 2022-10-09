import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()


def show_users():
    cursor.execute("select * from students")
    results = cursor.fetchall()
    return results


def add_user_model(data):
    print(data)
    surname, name, phone, description = data
    print(surname, name, phone, description)
    cursor.execute(
        f"insert into students (surname, name, phone, description)"
        f"values ('{surname}', '{name}', {phone}, '{description}')"
    )
    conn.commit()


def del_user_model(data):
    cursor.execute(
        f"delete from students where id={data}"
    )
    conn.commit()


def change_user(data):
    id, what_change, new_value = data
    if what_change == 'phone':
        int(new_value)
    cursor.execute(
        f"update students set '{what_change}'='{new_value}' where id={id}"
    )
    conn.commit()
   
