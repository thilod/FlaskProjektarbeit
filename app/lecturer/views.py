from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login import login_required



# define the blueprint
bp_lecturer = Blueprint('lecturer', __name__, template_folder='pages')


# all routes

# index is list view
@bp_lecturer.route('/')
@login_required
def home():
    return render_template('testpage.html')

