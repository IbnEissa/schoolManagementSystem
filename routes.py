from flask import Blueprint, render_template, request, redirect, url_for, flash
from controllers.student_controller import StudentsController

routes = Blueprint('routes', __name__)


@routes.route('/')
def index():
    students = StudentsController.get_all_students()
    return render_template('index2.html', students=students)


@routes.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        flash("Data Inserted Successfully")
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        StudentsController.insert_student(name, email, phone)
        return redirect(url_for('routes.index'))


@routes.route('/delete/<string:id_data>', methods=['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    StudentsController.delete_student(id_data)
    return redirect(url_for('routes.index'))


@routes.route('/update', methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        StudentsController.update_student(id_data, name, email, phone)
        flash("Data Updated Successfully")
        return redirect(url_for('routes.index'))
