from flask_mysqldb import MySQL

mysql = MySQL()


class Student:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def save(self):
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO students (name, email, phone) VALUES (%s, %s, %s)",
                    (self.name, self.email, self.phone))
        mysql.connection.commit()

    @staticmethod
    def get_by_id(student_id):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM students WHERE id=%s", (student_id,))
        data = cur.fetchone()
        cur.close()
        if data:
            student = Student(data['name'], data['email'], data['phone'])
            return student
        return None

    def delete(self):
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM students WHERE id=%s", (self.id,))
        mysql.connection.commit()
