from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_user, login_required, logout_user
from . import models

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route("/")
def index():
    rows_per_page = 10
    page = request.args.get('page', 1, type=int)
    films = models.Film.query.paginate(page=page, per_page=rows_per_page)
    return render_template('index.html', films=films)


@main_blueprint.route("/login", methods=['GET', 'POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    print(username, password)

    if username and password:
        user = models.User.query.filter_by(username=username).first()
        print(user)
        if user and (user.password == password):
            login_user(user)
            return redirect("/main-page")
        else:
            flash("Incorrect username or password.")
    else:
        flash("Fill username and password fields")
    return render_template("login.html")


@main_blueprint.route('/main-page', methods=['GET', 'POST'])
@login_required
def main_films_page():
    return render_template('main.html')


@main_blueprint.route("/register", methods=['GET', 'POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    password2 = request.form.get('password2')

    if request.method == "POST":
        if not (username or password2 or password):
            flash("Fill all the fields")
        elif password != password2:
            flash("Passwords are not equal")
        else:
            new_user = models.User(username=username, password=password, is_admin=False)
            models.db.session.add(new_user)
            models.db.session.commit()
            return redirect('/login')

    return render_template("register.html")


@login_required
@main_blueprint.route("/logout", methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect('/')
