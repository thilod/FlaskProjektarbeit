from flask import Blueprint, render_template
users = Blueprint('users', __name__, template_folder='pages')

@users.route('/')
def index():
    return render_template('users.html')