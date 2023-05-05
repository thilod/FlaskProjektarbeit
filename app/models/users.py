from flask_mongoengine import MongoEngine

db = MongoEngine()


class BaseUser(db.Document):
    email =          db.StringField(required=True, primary_key=True)
    firstName =      db.StringField(required=True)
    lastName =       db.StringField(required=True)
    password =       db.StringField(required=True)
    active =         db.BooleanField(required=True, default=True)
    
    meta = {'allow_inheritance': True}


class Administrator(BaseUser):
    pass

class Student(BaseUser):
    pass

class Lecturer(BaseUser):
    pass