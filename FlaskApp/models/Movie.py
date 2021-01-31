from . import db
from datetime import datetime


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(256), unique=True)
    duration_in_min = db.Column(db.Integer, unique=False, nullable=False)
    director = db.Column(db.String(256), unique=False, nullable=False)
    year = db.Column(db.DateTime, default=datetime.now)