from flask import Flask, request
from flask_restx import Api

from .home_page_routes import main_blueprint
from .film_resources import FilmResource, FilmsResource
from .models import *


app = Flask(__name__)
api = Api()
app.register_blueprint(main_blueprint, url_prefix="")
api.init_app(app)
app.config.from_object("project.config.Config")
app.secret_key = "very secret key"
login_manager.init_app(app)
db.init_app(app)
api.add_resource(FilmResource, "/api/films/<int:film_id>", "/api/films/<string:genre_name>", "/api/film/")
api.add_resource(FilmsResource, "/api/films")
migrate.init_app(app, db)
