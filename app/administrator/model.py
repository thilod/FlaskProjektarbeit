from flask_mongoengine import MongoEngine

db = MongoEngine()

"""
class Book(db.Document):
    title = db.StringField(max_length=80, required=True)
    author = db.StringField(max_length=80, required=True)
    year = db.IntField()
"""