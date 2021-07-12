from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_migrate import Migrate


app = Flask(__name__)
#app.config.from_object("film_project.services.web.project.config.Config")
#app.config.from_pyfile('config.py')
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://hello_flask:hello_flask@db:5432/hello_flask_dev"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#engine = create_engine("postgresql://hello_flask:hello_flask@localhost:5433/hello_flask_dev")
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(10), unique=False, nullable=False)
    is_admin = db.Column(db.Boolean(), default=False, nullable=False)
    films = db.relationship('Film', backref='user', lazy=True)

    def __init__(self, username, password, is_admin):
        self.username = username
        self.password = password
        self.is_admin = is_admin

    def __repr__(self):
        return f"{self.username} {self.password} admin: {str(self.is_admin)}"


class Director(db.Model):
    __tablename__ = "directors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    surname = db.Column(db.String(50), unique=False, nullable=False)
    films = db.relationship('Film', backref='director', lazy=True)

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Genre(db.Model):
    __tablename__ = "genres"

    id = db.Column(db.Integer, primary_key=True)
    genre_name = db.Column(db.String(30), unique=False, nullable=False)
    film_genres = db.relationship('FilmToGenre', backref='genre', lazy=True)

    def __init__(self, genre_name):
        self.genre_name = genre_name


class Film(db.Model):
    __tablename__ = "films"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    director_id = db.Column(db.Integer, db.ForeignKey('directors.id'), nullable=True)
    name = db.Column(db.String(200), unique=False, nullable=False)
    release_date = db.Column(db.DateTime(), unique=False, nullable=False)
    rating = db.Column(db.Float, db.CheckConstraint("1<=rating<=10"), unique=False, nullable=False)
    poster_link = db.Column(db.Text, unique=False, nullable=False)
    description = db.Column(db.Text, unique=False, nullable=True)
    film_genres = db.relationship('FilmToGenre', backref='film', lazy=True)

    def __init__(self, user_id, name, release_date, rating, poster_link, **kwargs):
        self.user_id = user_id
        self.name = name
        self.release_date = release_date
        self.rating = rating
        self.poster_link = poster_link
        if kwargs is not None:
            self.description = kwargs.get('description')
            self.director_id = kwargs.get('director_id')


class FilmToGenre(db.Model):
    __tablename__ = "film_to_genre"

    id = db.Column(db.Integer, primary_key=True)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'), nullable=False)
    film_id = db.Column(db.Integer, db.ForeignKey('films.id'), nullable=True)

    def __init__(self, genre_id, film_id):
        self.genre_id = genre_id
        self.film_id = film_id


@app.route("/kek")
def kek():
    return "<h1>KEK<h1>"


@app.route("/")
def hello_world():
    return jsonify(hello="world")
