from application import app, db
from flask import render_template, url_for, redirect, request
from application.models import User, Movie


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    
    return render_template("register.html")


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
    