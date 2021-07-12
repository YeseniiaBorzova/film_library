from flask import Blueprint, render_template, jsonify
from . import models

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route("/kek")
def kek():
    return jsonify(json_list=[i.serialize for i in models.Film.query.all()])


@main_blueprint.route("/")
def hello_world():
    return
