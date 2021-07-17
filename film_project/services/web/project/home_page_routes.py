"""Module contains main routes of app, login, registration, home and main pages"""

import logging

from flask import Blueprint, render_template, request, redirect, flash
from flask_login import login_user, login_required, logout_user, current_user

from . import models


main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

logging.basicConfig(level=logging.INFO, filename="app_routes_logs.txt", filemode="a",
                    format='%(asctime)s:%(levelname)s:%(message)s')


@main_blueprint.route("/home")
def index():
    rows_per_page = 10
    page = request.args.get('page', 1, type=int)
    films = models.Film.query.paginate(page=page, per_page=rows_per_page)
    logging.info(f"Showing films to user")
    return render_template('index.html', films=films)


@main_blueprint.route("/login", methods=['GET', 'POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username and password:
        user = models.User.query.filter_by(username=username).first()
        if user and (user.password == password):
            login_user(user)
            logging.info(f"User with credentials {user.username} {user.password} was logged in")
            return redirect("/main-page")
        else:
            logging.warning(f"Were entered incorrect username or password: {username} {password}")
            flash("Incorrect username or password.")
    else:
        logging.warning(f"Username or password were left blank {username} {password}")
        flash("Fill username and password fields")
    return render_template("login.html")


@main_blueprint.route('/main-page', methods=['GET', 'POST'])
@login_required
def main_films_page():
    user = current_user

    all_films = {"name": set(), "genres": []}
    film_genre_join = models.db.session.query(models.Film, models.FilmToGenre, models.Genre).\
        outerjoin(models.FilmToGenre, models.Film.id == models.FilmToGenre.film_id).\
        outerjoin(models.Genre, models.FilmToGenre.genre_id == models.Genre.id).all()

    logging.info(f"Returning all films with genres")

    return render_template('main.html', cur_user=user, all_films=film_genre_join, data=all_films)


@main_blueprint.route("/register", methods=['GET', 'POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    password2 = request.form.get('password2')

    if request.method == "POST":
        if not (username or password2 or password):
            flash("Fill all the fields")
            logging.warning(f"Some fields were left blank {username} {password} {password2}")
        elif password != password2:
            logging.warning(f"Passwords are not equal {password} {password2}")
            flash("Passwords are not equal")
        else:
            new_user = models.User(username=username, password=password, is_admin=False)
            models.db.session.add(new_user)
            models.db.session.commit()

            logging.info(f"New user {new_user.username} was created")

            return redirect('/login')

    return render_template("register.html")


@login_required
@main_blueprint.route("/logout", methods=['GET', 'POST'])
def logout():
    logging.info(f"Logging out {current_user.username}")
    logout_user()
    return redirect('/home')
