from application import app, db
from flask import render_template, url_for, redirect, request
from werkzeug.security import generate_password_hash, check_password_hash
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


@app.route('/create_movie/', methods=('GET', 'POST'))
def create_movie():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        genre = request.form['genre']
        movie = Movie(title=title,
        description=description,
        genre=genre,
        )
        db.session.add(movie)
        db.session.commit()

        return redirect(url_for('index'))    
    return render_template('create_movie.html')


# Issue with edit function, only pulling the first word from the db
@app.route('/<int:movie_id>/edit_movie/', methods=('GET', 'POST'))
def edit_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        genre = request.form['genre']

        movie.title = title
        movie.description = description
        movie.genre = genre

        db.session.add(movie)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('edit_movie.html', movie=movie)


# Add a different way to confirm the user wishes to delete the record
@app.post('/<int:movie_id>/delete_movie/')
def delete_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('index'))


@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")


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
    