import os
from flask import Flask, render_template,json, request
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

@app.route('/signUp',methods=['POST'])
def signUp():
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
    if _name and _email and _password:
        return json.dumps({'html': '<span>All fields good !!</span>'})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})

@app.route('/login', methods=["GET", "POST"])
def Showlogin():
        return render_template('login.html')

@app.route('/admin', methods=["GET", "POST"])
def ShowAdmin():
        return render_template('adminpanel.html')

@app.route('/client', methods=["GET", "POST"])
def ShowClient():
        return render_template('clientpanel.html')

@app.route('/movies', methods=["GET", "POST"])
def ShowMovies():
        return render_template('movies.html')


if __name__ == "__main__":
    app.run()

