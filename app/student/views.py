from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login import login_required

from .model import Book
from .forms import BookForm

# define the blueprint
bp_student = Blueprint('student', __name__, template_folder='pages')


# all routes

# index is list view
@bp_student.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        search = request.form['search']
        print(search)
        return redirect('search/'+search)
    elif request.method == 'GET':
        courses = [['Testkurs1', 'Beeeeeeeeeeschreibung'], [
            'Testkurs2', 'Beeeeeeeeeeschreibung2'], ['Testkurs3', 'Beeeeeeeeeeschreibung3']]
        return render_template('my_courses.html', courses=courses, info=session)


# add new book form
@bp_student.route('search/<search>', methods=['GET', 'POST'])
@login_required
def search(search):
    if request.method == 'POST':
        search = request.form['search']
        courses = [['Testkurs1', 'Beeeeeeeeeeschreibung'], [
            'Testkurs2', 'Beeeeeeeeeeschreibung2'], ['Testkurs3', 'Beeeeeeeeeeschreibung3']]
        return render_template('search_results.html', courses=courses, info=session)
    elif request.method == 'GET':
        search = search
        courses = [['Testkurs1', 'Beeeeeeeeeeschreibung'], [
            'Testkurs2', 'Beeeeeeeeeeschreibung2'], ['Testkurs3', 'Beeeeeeeeeeschreibung3']]
        return render_template('search_results.html', courses=courses, info=session)

# add new book form


@bp_student.route('/course/<coursename>', methods=['GET', 'POST'])
@login_required
def course(coursename):
    data = "Data: "+coursename
    return render_template('course_details.html', data=data, info=session)


@bp_student.route('/finished_courses', methods=['GET', 'POST'])
@login_required
def finished_courses():
    courses = [['Testkurs1', 'Beeeeeeeeeeschreibung'], [
        'Testkurs2', 'Beeeeeeeeeeschreibung2'], ['Testkurs3', 'Beeeeeeeeeeschreibung3']]
    return render_template('finished_courses.html', courses=courses, info=session)
