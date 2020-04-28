from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login import login_required

from .model import Book
from .forms import BookForm

# define the blueprint
books = Blueprint('books', __name__, template_folder='pages')

# all routes
@books.route('/')
@login_required
def home():
    books = Book.objects.all()
    return render_template('list.html', books=books, info=session)


@books.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = BookForm(request.form)
    if request.method == 'POST':
        if form.validate():
            book = Book(title=form.title.data,author=form.author.data,year=form.year.data)
            book.save()
            flash("Book added successfully.", "success")
            return redirect(url_for('.home'))
    return render_template('form.html', form = form, info=session)

