from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login import login_required
from app.users.models import User


# define the blueprint
bp_administrator = Blueprint('administrator', __name__, template_folder='pages')


# all routes

# index is list view
@bp_administrator.route('/courseEdit')
@login_required
def home():
    return render_template('courseEdit.html')

# Benutzerverwaltung
@bp_administrator.route('/users')
@login_required
def users():
    benutzer = [['mail1', 'Hans Castorp'], ['mail2', 'Grenouille'], ['mail3', 'Tonio Kröger'], ['mail4', 'Raskolnikov']]
    return render_template('users.html', benutzer=benutzer, info=session)

@bp_administrator.route('/users/create')
@login_required
def user_create():
    return render_template('user_create.html', info=session)

@bp_administrator.route('/users/<username>')
@login_required
def users_username(username):
    data = "Data: " + username
    return render_template('user_edit.html', info=session, Data=data)


# Statistik

@bp_administrator.route('/statistics')
@login_required
def statistics():
    return render_template('statistics.html', info=session)

"""
# add new book form
@bp_student.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = BookForm(request.form)
    if request.method == 'POST':
        if form.validate():
            book = Book(title=form.title.data,
                        author=form.author.data, year=form.year.data)
            book.save()
            flash("Book added successfully.", "success")
            return redirect(url_for('.home'))
    return render_template('form.html', form=form, info=session)
"""