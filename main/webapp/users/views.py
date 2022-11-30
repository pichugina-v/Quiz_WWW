from flask import Blueprint, render_template

auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')
user_blueprint = Blueprint('user', __name__, url_prefix='/user')


@auth_blueprint.route('/login')
def login():
    return render_template('base.html')


@auth_blueprint.route('/process-log', methods=['POST'])
def process_log():
    return "Отправка формы аутентификации"


@auth_blueprint.route('/register')
def register():
    return "Регистрация"


@auth_blueprint.route('/process-reg', methods=['POST'])
def process_reg():
    return "Отправка формы регистрации"


@auth_blueprint.route('/logout')
def logout():
    return "Выход"

@user_blueprint.route('/profiles')
def user_list():
    return "Все пользователи"

@user_blueprint.route('/profiles/<int:user_id>')
def user(user_id):
    return "Профиль пользователя"
