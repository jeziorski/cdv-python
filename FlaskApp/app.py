from flask import Flask
from flask import Flask, render_template
from models import db
from flask import request


app = Flask(__name__)
@app.route("/")
def main():
    return render_template('index.html')

@app.route('/showSignUp', methods=["GET", "POST"])
def ShowSignUp():
    if request.form:
        print(request.form)
    return render_template('signup.html')

if __name__ == "__main__":
    app.run()


