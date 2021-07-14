"""Module responsible for various resources that responsible
for GET, POST, DELETE request processing on Film, Director models"""

from flask import jsonify, abort, request
from flask_restx import Resource


from . import models


class FilmResource(Resource):
    """Resource responsible getting film by id, adding new film, deleting film by id"""

    def get(self, film_id):
        """GET request returns Film in JSON format by id"""
        film = models.Film.query.filter_by(id=film_id).first()
        if not film:
            abort(404)
        return jsonify(film.serialize)

    def post(self):
        """POST request creates new film in database"""
        user_id = request.json["user_id"]
        name = request.json["name"]
        release_date = request.json["release_date"]
        rating = request.json['rating']
        poster_link = request.json['poster_link']
        description = request.json.get('description', '')
        director_id = request.json.get('director_id', None)
        res = models.Film.query.filter_by(name=name).first()
        print(res)
        if rating > 10 or rating < 1:
            abort(400)
        if res:
            abort(409)
        new_film = models.Film(user_id=user_id, name=name, release_date=release_date,
                               rating=rating, poster_link=poster_link,
                               description=description, director_id=director_id)
        models.db.session.add(new_film)
        models.db.session.commit()
        return jsonify(new_film.serialize)

    def delete(self, film_id):
        """DELETE request deletes Film by id"""
        film = models.Film.query.get_or_404(film_id)
        models.db.session.delete(film)
        models.db.session.commit()
        return "", 204


class FilmDirector(Resource):
    """Resource responsible for searching films of director by id"""
    def get(self, director_id):
        """GET request returns all films of specified director by is"""
        film_directors = models.db.session.query(models.Film, models.Director).\
            join(models.Director, models.Film.director_id == models.Director.id).\
            filter(models.Director.id == director_id).all()

        films = []
        for film, director in film_directors:
            films.append(film)

        return jsonify({f"{director_id}": [i.serialize for i in films]})


class FilmGenre(Resource):
    def get(self, genre_name):
        """GET request returns all Films in JSON that belong to specified genre"""
        film_genre_join = models.db.session.query(models.Film, models.FilmToGenre, models.Genre). \
            join(models.FilmToGenre, models.Film.id == models.FilmToGenre.film_id). \
            join(models.Genre, models.FilmToGenre.genre_id == models.Genre.id).\
            filter(models.Genre.genre_name == genre_name).all()
        films = []
        for film, ft, genre in film_genre_join:
            films.append(film)

        return jsonify({f"{genre_name}": [i.serialize for i in films]})


class FilmsOrderByRatingDesc(Resource):
    """Resource responsible for sorting films by rating from 10 to 1"""
    def get(self):
        """GET request returns films list sorted by descending rating"""
        films = models.db.session.query(models.Film).order_by(models.Film.rating.desc())
        return jsonify(films=[i.serialize for i in films])


class FilmsOrderByDateDesc(Resource):
    """Resource responsible for sorting films by date from newest to oldest"""
    def get(self):
        """GET request returns films list sorted by descending release date"""
        films = models.db.session.query(models.Film).order_by(models.Film.release_date.desc())
        return jsonify(films=[i.serialize for i in films])


class FilmsOrderByRatingAsc(Resource):
    """Resource responsible for sorting films by rating from 1 to 10"""
    def get(self):
        """GET request returns films list sorted by ascending rating"""
        films = models.db.session.query(models.Film).order_by(models.Film.rating.asc())
        return jsonify(films=[i.serialize for i in films])


class FilmsOrderByDateAsc(Resource):
    """Resource responsible for sorting films by date from oldest to newest"""
    def get(self):
        """GET request returns films list sorted by ascending release date"""
        films = models.db.session.query(models.Film).order_by(models.Film.release_date.asc())
        return jsonify(films=[i.serialize for i in films])


class FilmsResource(Resource):
    """Resource responsible for returning of all films"""
    def get(self):
        """GET request returns all Films in JSON"""
        films = models.Film.query.all()
        return jsonify(list=[i.serialize for i in films])


class DirectorResource(Resource):
    """Resource responsible for GET, POST and DELETE request with director"""
    def get(self, director_id):
        """GET request returns Film in JSON format by id"""
        director = models.Director.query.filter_by(id=director_id).first()
        if not director:
            abort(404)
        return jsonify(director.serialize)

    def post(self):
        """POST request creates new director in database"""
        name = request.json["name"]
        surname = request.json["surname"]
        new_director = models.Director(name=name, surname=surname)
        models.db.session.add(new_director)
        models.db.session.commit()
        return jsonify(new_director.serialize)

    def delete(self, director_id):
        """DELETE request deletes director by id"""
        director = models.Director.query.get_or_404(director_id)
        models.db.session.query(models.Film).filter(models.Film.director_id == director.id).\
            update({models.Film.director_id: None})
        models.db.session.delete(director)
        models.db.session.commit()
        return "", 204
