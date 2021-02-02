import os
from db import User, Reservation, Movie
from flask import Flask, render_template, json, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from datetime import datetime

app = Flask(__name__)
#project_dir = os.path.dirname(os.path.abspath(__file__)) ## Obstawiam ze to bedzie do wyjebania
#database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabase.db"))## To tez
#app.config["SQLALCHEMY_DATABASE_URI"] = database_file #### i to do ogarniecia
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

def AllMovies():
    con = sqlite3.connect('cinema.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    movie_list = cur.execute(
        """
        SELECT id, title, date, start_time, duration_in_min, director, seats, price FROM Movie
        """)
    return movie_list
app = Flask(__name__)
@app.route("/")
def main():
    movie_list = AllMovies()
    return render_template('index.html', movie_list=movie_list)

@app.route('/showSignUp', methods=["GET", "POST"])
def ShowSignUp():
    if request.form:
        print(request.form)
    return render_template('signup.html')


@app.route('/signUp', methods=["GET", "POST"])
def signUp():
    if request.method == 'POST':
        req = request.form

        _name = request.form['Name']
        _email = request.form['Email']
        _password = request.form['Password']

        missing = list()

        for k, v in req.items():
            if v == "":
                missing.append(k)

        if missing:
            feedback = "Missing fields!"
            return render_template("signup.html", feedback=feedback)
        success = "Now you can log in"
        con = sqlite3.connect('cinema.db')
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute('INSERT INTO User VALUES(NULL, ?, ?, ?, ?);', (_name, _email, _password, datetime.now()))
        con.commit()
        con.close()
        #return redirect(request.url)
        return render_template("signup.html", success=success)
    return render_template("signup.html")


@app.route('/login', methods=["GET", "POST"])
def Showlogin():
        return render_template('login.html')

@app.route('/logging', methods=["GET", "POST"])
def Logging():
    if request.method == 'POST':
        req = request.form

        _email = request.form['Email']
        _password = request.form['Password']

        missing = list()

        for k, v in req.items():
            if v == "":
                missing.append(k)

        if missing:
            feedback = "Missing fields!"
            return render_template("login.html", feedback=feedback)

        return redirect(request.url)
        #db.session.add(user)
        #if zle dane pokaz błąd

        #if dobre dane przekieruj
        return redirect('/admin')
    return redirect('/admin')



@app.route('/admin', methods=["GET", "POST"])
def ShowAdmin():
    movie_list = AllMovies()
    return render_template('adminpanel.html', movie_list=movie_list)


@app.route('/client', methods=["GET", "POST"])
def ShowClient():
    movie_list=AllMovies()
    price1=AllMovies()
    return render_template('clientpanel.html', movie_list=movie_list, price1=price1)


@app.route('/movies', methods=["GET", "POST"])
def ShowMovies():
    movie_list = AllMovies()
    return render_template('movies.html', movie_list = movie_list)


@app.route('/addmovie', methods=["GET", "POST"])
def AddMovie():
    if request.method == 'POST':

        _title = request.form['Title']
        _date = request.form['Date']
        _start_time = request.form['Time']
        _duration_in_min = request.form['Duration']
        _director = request.form['Director']
        _seats = request.form['Seats']
        _price = request.form['Price']

        con = sqlite3.connect('cinema.db')
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute('INSERT INTO Movie VALUES(NULL, ?, ?, ?, ?, ?, ?, ?);', (_title, _date, _start_time, _duration_in_min,
                                                                        _director, _seats, _price))

        con.commit()
        return redirect('/admin')
    return redirect('/admin')


@app.route('/deletemovie', methods=["GET","POST"])
def DeleteMovie():
    _movieID = request.form['Id']
    con = sqlite3.connect('cinema.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute('DELETE FROM Movie WHERE id=?', (_movieID))
    con.commit()
    return redirect('/admin')

@app.route('/updatemovie', methods=["GET","POST"])
def UpdateMovie():
    if request.method == 'POST':
        _movie_id = request.form['Id']
        _title = request.form['Title']
        _date = request.form['Date']
        _start_time = request.form['Time']
        _duration_in_min = request.form['Duration']
        _director = request.form['Director']
        _seats = request.form['Seats']
        _price = request.form['Price']

        con = sqlite3.connect('cinema.db')
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute('UPDATE Movie SET title=?, date=?, start_time=? , duration_in_min=?, director=?, seats=?, price=? WHERE id=?', (_title, _date, _start_time , _duration_in_min, _director, _seats, _price, _movie_id))

        con.commit()
        return redirect('/admin')
    return redirect('/admin')


@app.route('/reserve', methods=["GET", "POST"])
def Reserve():
    if request.method == 'POST':

        _title = request.form['title']
        _seats = request.form['inputSeats']
        _name = request.form['name']
        _email = request.form['email']
        _total_price = request.form['totalPrice']
        con = sqlite3.connect('cinema.db')
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute('INSERT INTO Reservation VALUES(NULL, ?, ?, ?, ?, ?);', (_name, _email, _title, _seats, _total_price ))

        con.commit()
        return redirect('/client')
    return redirect('/client')

@app.errorhandler(404)
def not_found(error):
    return render_template('error404.html'), 404

if __name__ == "__main__":
    app.run()