from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    key = db.Column(db.String(256))
    notes = db.relationship('Note')

class EnviromentDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    humidity = db.Column(db.String(100))
    dateTime = db.Column(db.String(32))
    location = db.Column(db.String(32))

