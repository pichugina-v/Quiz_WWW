from flask import Blueprint, render_template

blueprint = Blueprint('quiz', __name__, url_prefix='/quiz')

@blueprint.route('/')
def quiz_info():
    page_title = 'Правила игры'
    return render_template(
        'quiz/quiz_info.html',
        page_title=page_title
    )


@blueprint.route('/<int:qz_id>/question/<int:qu_id>',  methods=['GET', 'POST'])
def question(qz_id, qu_id):
    return "Здесь будет номер вопроса по айдишке. Айди записывается в бд, для избежания повторов"


@blueprint.route('/<int:qz_id>/results', methods=['GET'])
def results(qz_id):
    return "Здесь будут результаты и верные ответы"