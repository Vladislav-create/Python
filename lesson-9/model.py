def get_contacts(cursor):
    cursor.execute("select * from students")
    results = cursor.fetchall()
    return results


def add_student(data, conn, cursor):
    surname, name, phone, description = data
    cursor.execute(
        f"insert into students (surname, name, phone, description)"
        f"values ('{surname}', '{name}', '{phone}', '{description}')"
    )
    conn.commit()



