from application import app, db
from flask import render_template, url_for, redirect, request
from application.models import Movie


@app.route('/add_movie')
def add_movie():
    new_movie = Movie(title="Saw",description="Scary movie",genre="Horror")
    db.session.add(new_movie)
    db.session.commit()
    return "Added new movie to database"

@app.route("/")
def index():
    movies = Movie.query.all()
    return render_template("index.html", movies=movies)


@app.route('/<int:movie_id>/')
def movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    return render_template('movie.html', movie=movie)


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
    