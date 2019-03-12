from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, ValidationError

class BookForm(FlaskForm):
    title = StringField('Book Title',validators=[DataRequired()])
    author = StringField('Author',validators=[DataRequired()])
    year = IntegerField('Year',validators=[DataRequired()])
    create = SubmitField('Create')
