from wtforms import (
    Form, StringField,
    EmailField, PasswordField,
    SubmitField
)
from wtforms.validators import (
    Optional, InputRequired,
    Email, DataRequired
)


class UserForm(Form):
    first_name = StringField('Имя', validators=[Optional()])
    last_name = StringField('Фамилия', validators=[Optional()])
    username = StringField(
        'Username', validators=[InputRequired(
            message='Это поле обязательно'
        )]
    )
    email = EmailField(
        'Email', validators=[InputRequired(
            message='Это поле обязательно'
        ), Email()]
    ),
    password = PasswordField(
        'Пароль', validators=DataRequired(
            message='Это поле обязательно'
        )
    )
    submit = SubmitField('Отправить')
