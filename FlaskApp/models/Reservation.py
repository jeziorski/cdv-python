from . import db
from datetime import datetime
from sqlalchemy import Table, Column, Integer, ForeignKey


class Reservation(db.Model):
    __tablename__ = 'reservation'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('User.id'))
    movie_id = db.Column(db.Integer, ForeignKey('Movie.id'))
    res_date = db.Column(db.DateTime, default=datetime.now)
