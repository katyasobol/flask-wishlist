import psycopg2
import base64
from flask import render_template, redirect, request, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash

from app import db, login_manager
from app.profiles import blueprint
from app.profiles.forms import LoginForm, RegisterForm, validate_date, verify_img
from app.profiles.models import User, Profile

@blueprint.route('/', methods=['POST', 'GET'])
def main():
    return 'hello'

@blueprint.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if request.method == "POST" and form.validate_on_submit() and verify_img(request.files['image'].filename):
        try:
            password_hash = generate_password_hash(request.form['password'])
            u = User(user=request.form['username'], email=request.form['email'], password=password_hash)
            db.session.add(u)
            db.session.flush()
            image = base64.b64encode(request.files['image'].read())
            p = Profile(firstname=request.form['firstname'], lastname=request.form
            ['lastname'], birthdate=request.form['birthdate'], user_id=u.id, image=image)
            db.session.add(p)
            db.session.commit()
        except:
            db.session.rollback()
            print("Ошибка добавления в БД")
            return render_template('layout/page-404.html')
        return redirect(url_for('profiles.login'))
    return render_template('profiles/register.html', form=form)


@blueprint.route('/login', methods=['POST', 'GET']) 
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        username = request.form.get('username')
        password = request.form.get('password')
        for user in db.session.query(User).where(User.user == username):
            if username == user.user and check_password_hash(user.password, password):
                login_user(user=user)
                return redirect(url_for('profiles.profile', user_id=current_user.id))
            else:
                flash('Неверная пара логин/пароль', 'error')
    return render_template('profiles/login.html', form=form)  


@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('ВСТАВИТЬ ССЫЛКУ НА ГЛАВНУЮ СТРАНИЦУ')) 


@blueprint.route('/<int:user_id>', methods=['POST', 'GET'])
@login_required
def profile(user_id):
    if current_user.is_authenticated:
        #image = None
        for form in db.session.query(Profile).where(Profile.user_id == current_user.id):
            image = base64.b64decode(form.image)
        return render_template('profiles/profile.html', form=form, image=image)
    return redirect(url_for('profiles.login')) 


@blueprint.route('/<int:user_id>/update', methods=['POST', 'GET'])
@login_required
def prof_upd(user_id):
    if request.method == 'POST' and current_user.is_authenticated:
        for user in db.session.query(Profile).where(Profile.user_id == current_user.id):
            user.firstname = request.form['firstname'] if request.form.get('firstname') else user.firstname
            user.lastname = request.form['lastname'] if request.form.get('lastname') else user.lastname
            user.birthdate = request.form['birthdate'] if request.form.get('birthdate') and validate_date(request['birthdate']) else user.birthdate
            user.image = base64.b64encode(request.files['image'].read()) if request.files.get('image') else user.image
        return redirect(url_for('profiles.profile', user_id=current_user.id))
    return render_template('profiles/profile_upd.html', user_id=current_user.id)


@login_manager.unauthorized_handler
def unauthorized_handler():
    return render_template('layout/page-403.html'), 403


@blueprint.errorhandler(403)
def access_forbidden(error):
    return render_template('layout/page-403.html'), 403


@blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('layout/page-404.html'), 404


@blueprint.errorhandler(500)
def internal_error(error):
    return render_template('layout/page-500.html'), 500