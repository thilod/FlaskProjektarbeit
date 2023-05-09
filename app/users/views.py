from flask import Blueprint, render_template, session
from app.users.models import User

bp_users = Blueprint('users', __name__, template_folder='pages')


# display users
"""
@bp_users.route('/')
def index():
    users = User.objects()

    return render_template('users_old.html', users=users, info=session)
"""