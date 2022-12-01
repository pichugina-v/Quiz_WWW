from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager

from main.db import db

from .webapp.user.models import User
from .webapp.home.views import blueprint as home_blueprint
from .webapp.quiz.views import blueprint as quiz_blueprint
from .webapp.user.views import auth_blueprint as auth_blueprint
from .webapp.user.views import user_blueprint as user_blueprint

def create_app():
    app = Flask(__name__, template_folder='webapp/templates', static_folder='webapp/static')
    app.config.from_pyfile('config.py')
    db.init_app(app)
    Migrate(app, db, render_as_batch=True)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    app.register_blueprint(home_blueprint)
    app.register_blueprint(quiz_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(user_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app

app = create_app()