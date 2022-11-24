from application import app, db
from flask import render_template, url_for, redirect, request, session, flash
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
from application.models import Movie, User, LoginForm, RegisterForm

bcrypt = Bcrypt(app)

@app.route('/add_movie')
def add_movie():
    new_movie = Movie(title="Saw",description="Scary movie",genre="Horror")
    db.session.add(new_movie)
    db.session.commit()
    return "Added new movie to database"


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('dashboard'))
    return render_template('login.html', form=form)


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', form=form)


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


@app.route("/movies")
def movies():
    return render_template("movies.html")


@app.route("/account")
def account():
    return render_template("account.html")
    