from flask import Flask
from flask_migrate import Migrate
from flask_restx import Api

from .main_page import main_blueprint
from .models import db


app = Flask(__name__)
api = Api()
app.register_blueprint(main_blueprint, url_prefix="")
api.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://hello_flask:hello_flask@db:5432/hello_flask_dev"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['FLASK_ENV'] = 'development'
db.init_app(app)
migrate = Migrate(app, db)
