from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login import login_required

from .model import Book
from .forms import BookForm


"""
# define the blueprint
bp_student = Blueprint('student', __name__, template_folder='pages')


# all routes

# index is list view
@bp_student.route('/')
@login_required
def home():
    books = Book.objects.all()
    return render_template('list.html', books=books, info=session)


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