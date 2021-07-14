from flask import jsonify, abort, request
from flask_restx import Resource, reqparse
from flask_login import login_required

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


class FilmsResource(Resource):
    """GET request returns all Films in JSON"""
    def get(self):
        films = models.Film.query.all()
        return jsonify(list=[i.serialize for i in films])


class DirectorResource(Resource):
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
