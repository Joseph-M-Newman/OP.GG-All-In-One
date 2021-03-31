import time
from datetime import timedelta
import flask 
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder="public", static_url_path="")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(minutes=5)

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    user = db.Column("user",db.String(100))
    password = db.Column("password", db.String(100))

    def __init__(self, user, password):
        self.user = user
        self.password = password


@app.route("/")
def home():
    return flask.render_template("index.html")

@app.route("/rocketleague")
def rocketleague():
    return flask.render_template("rocketleague.html")

@app.route("/league", methods=["POST","GET"])
def league():
    msg = None
    if request.method =="POST":
        return flask.render_template("league.html", )
    return flask.render_template("league.html")

@app.route("/valorant")
def valorant():
    return flask.render_template("valorant.html")

@app.route("/test")
def test():
    usr = users("joseph","password")
    db.session.add(usr)
    db.session.commit()
    userFound = users.query.filter_by(user="joseph").first()
    print(userFound.password)
    return flask.render_template("index.html")

# === run the server == default port localhost:5000 === (put on heroku to use site live)  
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)


