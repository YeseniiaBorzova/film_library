from flask import Flask
from flask_migrate import Migrate
from flask_restx import Api

from .main_page import main_blueprint
from .models import *


app = Flask(__name__)
api = Api()
app.register_blueprint(main_blueprint, url_prefix="")
api.init_app(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://hello_flask:hello_flask@localhost:5432/hello_flask_dev"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['FLASK_ENV'] = 'development'
app.config.from_object("project.config.Config")
app.secret_key = "very secret key"
login_manager.init_app(app)
db.init_app(app)
migrate.init_app(app, db)
