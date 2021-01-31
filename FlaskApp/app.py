import os
from models import User
from flask import Flask, render_template, json, request, redirect
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabase.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)


app = Flask(__name__)
@app.route("/")
def main():
    return render_template('index.html')

@app.route('/showSignUp', methods=["GET", "POST"])
def ShowSignUp():
    if request.form:
        print(request.form)
    return render_template('signup.html')

@app.route('/signUp',methods=["GET", "POST"])
def signUp():
    if request.method == 'POST':
        req = request.form

        _name = request.form['Name']
        _email = request.form['Email']
        _password = request.form['Password']
        user = User(_name, _email, _password)
        missing = list()

        for k, v in req.items():
            if v == "":
                missing.append(k)

        if missing:
            feedback = "Missing fields!"
            return render_template("signup.html", feedback=feedback)

        return redirect(request.url)
        db.session.add(user)
        success = "Now you can login"
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
        return render_template("login.html", success=success)
    return render_template("login.html")

@app.route('/admin', methods=["GET", "POST"])
def ShowAdmin():
        return render_template('adminpanel.html')

@app.route('/client', methods=["GET", "POST"])
def ShowClient():
        return render_template('clientpanel.html')

@app.route('/movies', methods=["GET", "POST"])
def ShowMovies():
        return render_template('movies.html')

@app.route('/addmovie', methods=["GET","POST"])
def AddMovie():
    _movieID = request.form['']
    Movie.select().where(Movie.id == _movieID).get().delete_instance()
    return render_template('adminpanel.html')

@app.route('/deletemovie', methods=["GET","POST"])
def DeleteMovie():
    _movieID = request.form['deleteID']
    Movie.select().where(Movie.id == _movieID).get().delete_instance()
    return render_template('adminpanel.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('error404.html'), 404

if __name__ == "__main__":
    app.run()

