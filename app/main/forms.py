from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms import validators
from werkzeug.security import check_password_hash

from app.users.models import User


class LoginForm(FlaskForm):
    """
    The login form
    """
    username = StringField(u'Username', validators=[validators.DataRequired()])
    password = PasswordField(u'Password', validators=[validators.optional()])

    def validate(self):
        check_validate = super(LoginForm, self).validate()

        # if our validators do not pass
        if not check_validate:
            return False

        # does our user exist?
        user = User.objects.get(username=self.username.data)
        if not user:
            self.username.errors.append('Invalid username or password')
            return False

        # do the passwords match
        if not check_password_hash(user.password,self.password.data):
            self.username.errors.append('Invalid username or password')
            return False

        return True
