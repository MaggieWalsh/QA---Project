from flask import Flask
from application import app
from application.models import Movie


if __name__ == '__main__':
    app.run(debug=True)