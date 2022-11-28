from flask import Blueprint, current_app

blueprint = Blueprint('home', __name__)

@blueprint.route('/')
def index():
    return "Index"