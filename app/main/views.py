import flask
from flask import Blueprint, render_template, flash, redirect, request, url_for, session
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

from app.main.forms import LoginForm
from app.users.models import User

bp_main = Blueprint('main', __name__, template_folder='pages',
                    static_folder='main-static')

# all routes


# index page
@bp_main.route('/')
def home():
    return render_template('index.html', info=session)


# login page
@bp_main.route("/login", methods=["GET", "POST"])
def login():

    # get form
    form = LoginForm()
    error_msg = None

    # when called with filled form
    if flask.request.method == 'POST':

        if form.validate_on_submit():
            user = User.objects.get(username=form.username.data)
            login_user(user)
            session['username'] = form.username.data
            flash("Logged in successfully.", "success")
            next_page = request.args.get('next')
            return redirect(next_page or url_for(".home"))
        else:
            error_msg = "Login incorrect."

    return render_template("login.html", form=form, info=session, error=error_msg)


# logout page
@bp_main.route("/logout")
def logout():
    logout_user()
    session.pop('username', None)
    flash("You have been logged out.", "success")
    return redirect(url_for(".home"))


@bp_main.route("/restricted")
@login_required
def restricted():
    return "You can only see this if you are logged in!", 200
