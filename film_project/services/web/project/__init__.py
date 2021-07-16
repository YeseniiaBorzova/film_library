from flask import Flask, request
from flask_restx import Api

from .home_page_routes import main_blueprint
from .film_resources import *

from .models import *


app = Flask(__name__)
api = Api()
app.register_blueprint(main_blueprint, url_prefix="")
app.register_blueprint(films_blueprint, url_prefix="")
api.init_app(app)
app.config.from_object("project.config.Config")
app.secret_key = "very secret key"
login_manager.init_app(app)
db.init_app(app)
api.add_resource(FilmResource, "/api/films/<int:film_id>", "/api/film/")
api.add_resource(FilmsResource, "/api/films")
api.add_resource(FilmGenre, "/api/films/<string:genre_name>")
api.add_resource(FilmDirectorById, "/api/films/director-film/<int:director_id>")
api.add_resource(FilmDirectorByFullName, "/api/films/director-film/")
api.add_resource(FilmsOrderByRatingDesc, "/api/films/order-by-rating-desc")
api.add_resource(FilmsOrderByDateDesc, "/api/films/order-by-date-desc")
api.add_resource(FilmsOrderByRatingAsc, "/api/films/order-by-rating-asc")
api.add_resource(FilmsOrderByDateAsc, "/api/films/order-by-date-asc")
api.add_resource(DirectorResource, "/api/directors/<int:director_id>", "/api/director/")
migrate.init_app(app, db)
