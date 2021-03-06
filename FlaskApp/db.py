import os
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, date
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import *

metadata = MetaData()

if os.path.exists('cinema.db'):
    os.remove('cinema.db')
# tworzymy instancję klasy Engine do obsługi bazy
baza = create_engine('sqlite:///cinema.db')  # ':memory:'



# klasa bazowa
Model = declarative_base()


class User(Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(256), unique=True, nullable=False)
    email = Column(String(256), nullable=False)
    password = Column(String(256), nullable=False)
    creation_date = Column(DateTime, default=datetime.now)


class Reservation(Model):
    __tablename__ = 'reservation'
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    email = Column(String(256), nullable=False)
    title = Column(String(256),nullable=False)
    tickets = Column(Integer, nullable=False)
    total_price = Column(Integer, nullable=False)
    date = Column(Date)
    start_time = Column(String(256), nullable=False)

    #movie_id = Column(Integer, ForeignKey('movie.id'))
    #user_id = Column(Integer, ForeignKey('user.id'))


class Movie(Model):
    __tablename__ = 'movie'
    id = Column(Integer, primary_key=True)
    title = Column(String(256), nullable=False)
    date = Column(Date)
    start_time = Column(String(256), nullable=False)
    duration_in_min = Column(Integer, unique=False, nullable=False)
    director = Column(String(256), unique=False, nullable=False)
    seats = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)


#tworzenie tabel
Model.metadata.create_all(baza)

BDSession = sessionmaker(bind=baza)
session = BDSession()


if not session.query(User).count():
    session.add(User(username="jankowak12", email='jannowak@gmail.com', password="12345"))
    session.add(User(username="michalek1234", email='michalwer@gmail.com', password="asdfgh12"))


session.add_all([
    Movie(title="Taxi 3", date=date(2021,2,2), start_time='15:50', duration_in_min=120, director='Gérard Krawczyk', seats=80, price=20),
    Movie(title="Ocalony", date=date(2021,2,2), start_time='13:20', duration_in_min=134, director='Peter Berg', seats=100, price=20),
])

session.commit()

