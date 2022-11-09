import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/movies")
def movies():
    return render_template("movies.html")

@app.route("/shows")
def shows():
    return render_template("shows.html")


@app.route("/celebs")
def celebs():
    return render_template("celebs.html")


@app.route("/account")
def account():
    return render_template("account.html")
    

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )