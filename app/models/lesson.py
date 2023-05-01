from flask_mongoengine import MongoEngine
from app.models.course import Course
from app.models.users  import Lecturer
from app.models.users  import BaseUser

db = MongoEngine()


class Lesson(db.Document):
    course =       db.ReferenceField(Course)
    lecturer =     db.ReferenceField(Lecturer)
    participants = db.ListField(db.ReferenceField(BaseUser))
    date =         db.StringField(max_length=80,   required=True)
    description =  db.StringField(max_length=1000, required=True)
    maxStudents =  db.IntField(required=True)
    canceled =     db.BooleanField(default=False, required=True)