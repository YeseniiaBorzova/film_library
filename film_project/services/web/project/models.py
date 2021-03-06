"""Module contains all models defined in our database"""

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


class User(db.Model, UserMixin):
    """User model"""
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), unique=False, nullable=False)
    is_admin = db.Column(db.Boolean(), default=False, nullable=False)
    films = db.relationship('Film', backref='user', lazy=True)

    def __init__(self, username, password, is_admin):
        """Constructor"""
        self.username = username
        self.password = password
        self.is_admin = is_admin

    def __repr__(self):
        """Overriding string representation of an object"""
        return f"{self.username} {self.password} admin: {str(self.is_admin)}"

    @login_manager.user_loader
    def load_user(user_id):
        """Overriding method for flask login"""
        return User.query.get(user_id)

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'is admin': self.is_admin
        }


class Director(db.Model):
    """Director model"""
    __tablename__ = "directors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    surname = db.Column(db.String(50), unique=False, nullable=False)
    films = db.relationship('Film', backref='director', lazy=True)

    def __init__(self, name, surname):
        """Constructor"""
        self.name = name
        self.surname = surname

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname
        }


class Genre(db.Model):
    """Genre model"""
    __tablename__ = "genres"

    id = db.Column(db.Integer, primary_key=True)
    genre_name = db.Column(db.String(30), unique=False, nullable=False)
    film_genres = db.relationship('FilmToGenre', backref='genre', lazy=True)

    def __init__(self, genre_name):
        """Constructor"""
        self.genre_name = genre_name

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'genre name': self.genre_name
        }


class Film(db.Model):
    """Film model"""
    __tablename__ = "films"

    genres = []

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    director_id = db.Column(db.Integer, db.ForeignKey('directors.id'), nullable=True)
    name = db.Column(db.String(200), unique=False, nullable=False)
    release_date = db.Column(db.DateTime(), unique=False, nullable=False)
    rating = db.Column(db.Float, unique=False, nullable=False)
    poster_link = db.Column(db.Text, unique=False, nullable=False)
    description = db.Column(db.Text, unique=False, nullable=True)
    film_genres = db.relationship('FilmToGenre', backref='film', lazy=True)

    def __init__(self, user_id, name, release_date, rating, poster_link, **kwargs):
        """Constructor"""
        self.user_id = user_id
        self.name = name
        self.release_date = release_date
        self.rating = rating
        self.poster_link = poster_link
        if kwargs is not None:
            self.description = kwargs.get('description')
            self.director_id = kwargs.get('director_id')

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'director_id': self.director_id,
            'name': self.name,
            'release date': self.release_date,
            'rating': self.rating,
            'poster link': self.poster_link,
            'description': self.description
        }

    def add_genre(self, genre):
        """Adds genre in genres list"""
        self.genres.append(genre)

    def check_genre(self, genre):
        """Check if genre already present in genre list"""
        return genre in self.genres


class FilmToGenre(db.Model):
    """Model film to genre"""
    __tablename__ = "film_to_genre"

    id = db.Column(db.Integer, primary_key=True)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'), nullable=False)
    film_id = db.Column(db.Integer, db.ForeignKey('films.id'), nullable=True)

    def __init__(self, genre_id, film_id):
        """Constructor"""
        self.genre_id = genre_id
        self.film_id = film_id

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'film_id': self.film_id,
            'genre_id': self.genre_id
        }
