from flask import Flask

from .webapp.home.views import blueprint as home_blueprint
from .webapp.quiz.views import blueprint as quiz_blueprint
from .webapp.users.views import blueprint as user_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    app.register_blueprint(home_blueprint)
    app.register_blueprint(quiz_blueprint)
    app.register_blueprint(user_blueprint)
    return app

app = create_app()