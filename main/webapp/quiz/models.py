from main.db import db


quiz_question_table = db.Table(
    "quiz_question_table",
    db.Model.metadata,
    db.Column("quiz_id", db.ForeignKey("quizzes.id"), primary_key=True),
    db.Column("question_id", db.ForeignKey("questions.id"), primary_key=True),
)

class Quiz(db.Model):
    __tablename__ = 'quizzes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False
    )
    questions = db.relationship(
        'Question', secondary=quiz_question_table, back_populates='quizzes'
    )
    score = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return '<{id}: User: {user_id}, {score}>'.format(
            self.id, self.user_id, self.score
        )


class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    quizzes = db.relationship(
        'Quiz', secondary=quiz_question_table,back_populates='questions'
    )
    answers = db.relationship(
        'Answer', back_populates='questions', cascade='all, delete'
    )

    def __repr__(self):
        return '<{id}: {name}>'.format(self.id, self.name)


class Answers(db.Model):
    __tablename__= 'answers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    answers = db.relationship(
        'Question', back_populates='answers', cascade='all, delete'
    )
