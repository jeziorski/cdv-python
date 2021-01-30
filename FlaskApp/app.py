from flask import Flask
from flask import Flask, render_template
from models import db


app = Flask(__name__)
@app.route("/")
def main():
    return render_template('index.html')

@app.route('/showSignUp')
def ShowSignUp():
    return render_template('signup.html')

if __name__ == "__main__":
    app.run()


