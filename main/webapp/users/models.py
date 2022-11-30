from main.db import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    __table_args__ = (db.UniqueConstraint('username', 'password'),)

    def __repr__(self):
        return '<{id}: {username}, {email}>'.format(
            self.id, self.username, self.email
        )
