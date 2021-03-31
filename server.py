import time
import flask 
from flask import Flask, request, render_template
import mariadb
from flaskext.mysql import MySQL

app = Flask(__name__, static_folder="public", static_url_path="")

@app.route("/")
def home():
    return flask.render_template("index.html")

@app.route("/rocketleague")
def rocketleague():
    return flask.render_template("rocketleague.html")

@app.route("/league")
def league():
    return flask.render_template("league.html")

@app.route("/valorant")
def valorant():
    return flask.render_template("valorant.html")

# === run the server == default port localhost:5000 === (put on heroku to use site live)  
if __name__ == "__main__":
	app.run(debug=True)