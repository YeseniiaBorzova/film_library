from flask import Flask
from flask_migrate import Migrate
from .main_page import main_blueprint
from .models import db


app = Flask(__name__)
app.register_blueprint(main_blueprint, url_prefix="")
#app.config.from_object("film_project.services.web.project.config.Config")
#app.config.from_pyfile('config.py')
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://hello_flask:hello_flask@db:5432/hello_flask_dev"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
#engine = create_engine("postgresql://hello_flask:hello_flask@localhost:5433/hello_flask_dev")

migrate = Migrate(app, db)
