from flask import jsonify, abort, request
from flask_restx import Resource, reqparse

from . import models


class FilmResource(Resource):
    def get(self, film_id):
        film = models.Film.query.get_or_404(film_id)
        if not film:
            abort(404)
        return jsonify(film.serialize)

    def get(self, genre_name):
        film_genre_join = models.db.session.query(models.Film, models.FilmToGenre, models.Genre). \
            join(models.FilmToGenre, models.Film.id == models.FilmToGenre.film_id). \
            join(models.Genre, models.FilmToGenre.genre_id == models.Genre.id).\
            filter(models.Genre.genre_name == genre_name).all()
        films = []
        for film, ft, genre in film_genre_join:
            films.append(film)

        return jsonify({f"{genre_name}": [i.serialize for i in films]})

    def post(self):
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
        film = models.Film.query.get_or_404(film_id)
        models.db.session.delete(film)
        models.db.session.commit()
        return "", 204


class FilmsResource(Resource):
    def get(self):
        films = models.Film.query.all()
        return jsonify(list=[i.serialize for i in films])
