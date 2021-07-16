"""Module responsible for various resources that responsible
for GET, PUT, POST, DELETE request processing on Film, Director models"""

from flask import jsonify, abort, request, Blueprint
from flask_restx import Resource
from flask_httpauth import HTTPBasicAuth


from . import models


auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    """Redefined method for http_auth to verify user"""
    user = models.User.query.filter_by(username=username).first()
    if user and user.password == password:
        return True
    return False


def get_paginated_list(results, url, start, limit):
    """Function responsible for pagination of JSON film object on GET request by url '/api/films'"""
    start = int(start)
    limit = int(limit)
    count = len(results)
    if count < start or limit < 0:
        abort(404)

    obj = {'start': start, 'limit': limit, 'count': count}
    if start == 1:
        obj['previous'] = ''
    else:
        start_copy = max(1, start - limit)
        limit_copy = start - 1
        obj['previous'] = url + '?start=%d&limit=%d' % (start_copy, limit_copy)

    if start + limit > count:
        obj['next'] = ''
    else:
        start_copy = start + limit
        obj['next'] = url + '?start=%d&limit=%d' % (start_copy, limit)

    obj['results'] = results[(start - 1):(start - 1 + limit)]
    return obj


class FilmResource(Resource):
    """Resource responsible getting film by id, adding new film, deleting film by id"""

    def get(self, film_id):
        """GET request returns Film in JSON format by id"""
        film = models.Film.query.filter_by(id=film_id).first()
        if not film:
            abort(404)
        return jsonify(film.serialize)

    @auth.login_required
    def post(self):
        """POST request creates new film in database only for authorized users"""
        user = models.User.query.filter_by(username=auth.current_user()).first()
        director_name = request.json.get("director_name")
        director_surname = request.json.get("director_surname")
        if director_surname is not None:
            director = models.Director.query.filter_by(name=director_name, surname=director_surname).first()
            if director:
                director_id = director.id
            else:
                new_director = models.Director(name=director_name, surname=director_surname)
                models.db.session.add(new_director)
                director_id = models.Director.query.filter_by(name=director_name, surname=director_surname).first().id
                models.db.session.commit()
        else:
            director_id = None
        user_id = user.id
        name = request.json["name"]
        release_date = request.json["release_date"]
        rating = request.json['rating']
        poster_link = request.json['poster_link']
        description = request.json.get('description', '')
        res = models.Film.query.filter_by(name=name).first()
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

    @auth.login_required
    def put(self, film_id):
        """PUT request to change films rating, poster_link, name, director only by admin or user who added it"""
        user = models.User.query.filter_by(username=auth.current_user()).first()
        film = models.Film.query.get_or_404(film_id)
        rating = request.json.get('rating')
        poster_link = request.json.get('poster_link')
        name = request.json.get('name')
        director_name = request.json.get("director_name")
        director_surname = request.json.get("director_surname")
        if rating > 10 or rating < 1:
            abort(400)
        if film.user_id == user.id or user.is_admin:
            if rating:
                models.db.session.query(models.Film).filter(models.Film.id == film.id). \
                    update({models.Film.rating: rating})
                models.db.session.commit()

            if poster_link:
                models.db.session.query(models.Film).filter(models.Film.id == film.id). \
                    update({models.Film.poster_link: poster_link})
                models.db.session.commit()

            if name:
                models.db.session.query(models.Film).filter(models.Film.id == film.id). \
                    update({models.Film.name: name})
                models.db.session.commit()

            if director_name and director_surname:
                director = models.Director.query.filter_by(name=director_name, surname=director_surname).first()
                if director:
                    models.db.session.query(models.Film).filter(models.Film.id == film.id). \
                        update({models.Film.director_id: director.id})
                    models.db.session.commit()
                else:
                    new_director = models.Director(name=director_name, surname=director_surname)
                    models.db.session.add(new_director)
                    director_id = models.Director.query.filter_by(name=director_name,
                                                                  surname=director_surname).first().id
                    models.db.session.query(models.Film).filter(models.Film.id == film.id). \
                        update({models.Film.director_id: director_id})
                    models.db.session.commit()

        return jsonify(film.serialize)

    @auth.login_required
    def delete(self, film_id):
        """DELETE request deletes Film by id only by user that added it or admin"""
        user = models.User.query.filter_by(username=auth.current_user()).first()
        film = models.Film.query.get_or_404(film_id)
        if film.user_id == user.id or user.is_admin:
            models.db.session.delete(film)
            models.db.session.commit()
            return "", 204
        else:
            abort(403)


class FilmDirectorById(Resource):
    """Resource responsible for searching films of director by id"""
    def get(self, director_id):
        """GET request returns all films of specified director by is"""
        film_directors = models.db.session.query(models.Film, models.Director).\
            join(models.Director, models.Film.director_id == models.Director.id).\
            filter(models.Director.id == director_id).all()

        films = []
        for film, director in film_directors:
            films.append(film)

        if len(films) == 0:
            abort(404)

        return jsonify({f"{director_id}": [i.serialize for i in films]})


class FilmDirectorByFullName(Resource):
    """Resource responsible for getting director by full name"""
    def get(self):
        director_name = request.json["director_name"]
        director_surname = request.json["director_surname"]
        film_directors = models.db.session.query(models.Film, models.Director). \
            join(models.Director, models.Film.director_id == models.Director.id). \
            filter(models.Director.name == director_name, models.Director.surname == director_surname).all()

        films = []
        for film, director in film_directors:
            films.append(film)

        if len(films) == 0:
            abort(404)

        return jsonify({f"{director_name} {director_surname}": [i.serialize for i in films]})


class FilmGenre(Resource):
    """Resource returning all films that related to specified genre"""
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


class FilmOrderedByYears(Resource):
    """Resource responsible for returning films in some defined year range"""
    def get(self):
        """GET request returns films in some year range"""
        year_from = int(request.json['year_from'])
        year_to = int(request.json['year_to'])
        films = models.db.session.query(models.Film).\
            filter(models.db.extract('year', models.Film.release_date).between(year_from, year_to)).all()
        if len(films) == 0:
            abort(404)

        return jsonify({f"{year_from} - {year_to}": [i.serialize for i in films]})


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
        for film in films:
            if film.director_id is None:
                film.director_id = 'unknown'

        return jsonify(get_paginated_list(
            [i.serialize for i in films],
            '/api/films',
            start=request.args.get('start', 1),
            limit=request.args.get('limit', 10)
        ))


class DirectorResource(Resource):
    """Resource responsible for GET, POST and DELETE request with director"""
    def get(self, director_id):
        """GET request returns director in JSON format by id"""
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

    @auth.login_required
    def delete(self, director_id):
        """DELETE request deletes director by id only for admins"""
        user = models.User.query.filter_by(username=auth.current_user()).first()
        if user.is_admin:
            director = models.Director.query.get_or_404(director_id)
            models.db.session.query(models.Film).filter(models.Film.director_id == director.id).\
                update({models.Film.director_id: None})
            models.db.session.delete(director)
            models.db.session.commit()
            return "", 204
        elif not user.is_admin:
            abort(403)
