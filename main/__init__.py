from flask import Flask
from flask_migrate import Migrate

from .db import db

from .webapp.home.views import blueprint as home_blueprint
from .webapp.quiz.views import blueprint as quiz_blueprint
from .webapp.users.views import blueprint as user_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    Migrate(app, db)

    app.register_blueprint(home_blueprint)
    app.register_blueprint(quiz_blueprint)
    app.register_blueprint(user_blueprint)
    return app

app = create_app()