from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(10), unique=False, nullable=False)
    is_admin = db.Column(db.Boolean(), default=False, nullable=False)
    films = db.relationship('Film', backref='user', lazy=True)

    def __init__(self, username, password, **kwargs):
        self.username = username
        self.password = password
        if kwargs is not None:
            self.is_admin = kwargs['is_admin']


class Director(db.Model):
    __tablename__ = "directors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    surname = db.Column(db.String(50), unique=False, nullable=False)
    films = db.relationship('Film', backref='director', lazy=True)


class Genre(db.Model):
    __tablename__ = "genres"

    id = db.Column(db.Integer, primary_key=True)
    genre_name = db.Column(db.String(30), unique=False, nullable=False)
    film_genres = db.relationship('FilmToGenre', backref='genre', lazy=True)


class Film(db.Model):
    __tablename__ = "films"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'), nullable=True)
    name = db.Column(db.String(200), unique=False, nullable=False)
    release_date = db.Column(db.DateTime(), unique=False, nullable=False)
    rating = db.Column(db.Float, db.CheckConstraint("1<=rating<=10"), unique=False, nullable=False)
    poster_link = db.Column(db.Text, unique=False, nullable=False)
    description = db.Column(db.Text, unique=False, nullable=True)
    film_genres = db.relationship('FilmToGenre', backref='film', lazy=True)


class FilmToGenre(db.Model):
    __tablename__ = "film_to_genre"

    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'), nullable=False)
    film_id = db.Column(db.Integer, db.ForeignKey('film.id'), nullable=True)


@app.route("/")
def hello_world():
    return jsonify(hello="world")
