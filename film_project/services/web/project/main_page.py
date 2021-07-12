from flask import Blueprint, render_template, jsonify, request
from . import models

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route("/kek")
def kek():
    return jsonify(json_list=[i.serialize for i in models.Film.query.all()])


@main_blueprint.route("/")
def index():
    rows_per_page = 10
    page = request.args.get('page', 1, type=int)
    films = models.Film.query.paginate(page=page, per_page=rows_per_page)
    return render_template('index.html', films=films)
