from . import db
from datetime import datetime
from sqlalchemy import Table, Column, Integer, ForeignKey

class Reservation(db.Model):
    __tablename__ = 'reservation'
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, ForeignKey('Movie.id'))
    user_id = db.Column(db.Integer, ForeignKey('User.id'))
    email = db.Column(db.String(256), unique=True, nullable=False)
    tickets = db.Column(db.Integer, unique=False, nullable=False)


