from flask_mongoengine import MongoEngine

db = MongoEngine()


class Course(db.Document):
    name =        db.StringField(max_length=80,   required=True)
    description = db.StringField(max_length=1000, required=True)