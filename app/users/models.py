from flask_mongoengine import MongoEngine
from flask_login import UserMixin, login_manager

db = MongoEngine()


class User(db.Document, UserMixin):
    username = db.StringField(required=True,primary_key=True)
    password = db.StringField(required=True)

    def __repr__(self):
        return '<User %r>' % self.id
