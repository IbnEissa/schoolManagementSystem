from flask_mysqldb import MySQL
from models.student import Student

mysql = MySQL()


def get_all_students():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    cur.close()
    return data


def insert_student(name, email, phone):
    student = Student(name, email, phone)
    student.save()


def delete_student(id_data):
    student = Student.get_by_id(id_data)
    if student:
        student.delete()


def update_student(id_data, name, email, phone):
    student = Student.get_by_id(id_data)
    if student:
        student.name = name
        student.email = email
        student.phone = phone
        student.save()
