# Import the necessary modules
from flask import url_for
from flask_testing import TestCase

# import the app's classes and objects
from app import app, db, User, Movie


class TestBase(TestCase):

    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        db.create_all()

        test_movie = Movie(title="Saw",description="Scary movie",genre="Horror")

        db.session.add(test_movie)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()