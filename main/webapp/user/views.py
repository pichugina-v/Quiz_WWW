from flask import (
    Blueprint, render_template,
    redirect, url_for, flash
)
from flask_login import current_user, login_user, logout_user
from werkzeug.security import generate_password_hash

from .models import User
from .forms import RegistrationForm, LoginForm
from main.db import db

auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')
user_blueprint = Blueprint('user', __name__, url_prefix='/user')


@auth_blueprint.route('/login')
def login():
    page_title = 'Вход в аккаунт'
    form = LoginForm()
    return render_template(
        'auth/login.html',
        form=form,
        page_title=page_title
    )

@auth_blueprint.route('/process-log', methods=['POST'])
def process_log():
    form = LoginForm()

    if not form.validate_on_submit():
        flash('Неверное имя пользователя или пароль')
        return redirect(url_for('auth.login'))
    user = User.query.filter(User.username == form.username.data).first()
    if user and user.check_password(form.password.data):
        login_user(user=user)
        return redirect(url_for('home.index'))

@auth_blueprint.route('/register')
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home.index'))
    page_title = 'Регистрация'
    form = RegistrationForm()
    return render_template(
        'auth/register.html',
        form=form,
        page_title=page_title
    )

@auth_blueprint.route('/process-reg', methods=['POST'])
def process_reg():
    form = RegistrationForm()

    if form.validate_on_submit():
        new_user = User(
            username=form.username.data,
            email = form.email.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            password=generate_password_hash(form.password.data),
            role='user'
        )
        db.session.add(new_user)
        db.session.commit()
        flash('Вы успешно зарегистрировались')
    return redirect(url_for('home.index'))

@auth_blueprint.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
        flash('Вы вышли из аккаунта')
    return redirect(url_for('home.index'))

@user_blueprint.route('/profiles')
def user_list():
    return "Все пользователи"

@user_blueprint.route('/profiles/<int:user_id>')
def user(user_id):
    return "Профиль пользователя"
