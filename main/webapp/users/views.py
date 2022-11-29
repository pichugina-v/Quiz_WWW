from flask import Blueprint

blueprint = Blueprint('user', __name__, url_prefix='/user')


@blueprint.route('/login')
def login():
    return "Аутентификация"


@blueprint.route('/process-log', methods=['POST'])
def process_log():
    return "Отправка формы аутентификации"


@blueprint.route('/register')
def register():
    return "Регистрация"


@blueprint.route('/process-reg', methods=['POST'])
def process_reg():
    return "Отправка формы регистрации"


@blueprint.route('/logout')
def logout():
    return "Выход"