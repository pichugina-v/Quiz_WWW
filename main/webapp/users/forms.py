from wtforms import (
    Form, StringField,
    EmailField, PasswordField,
    SubmitField
)
from wtforms.validators import (
    Optional, Email,
    DataRequired, EqualTo
)


class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    sumbit = SubmitField('Отправить')


class RegistrationForm(Form):
    first_name = StringField('Имя', validators=[Optional()])
    last_name = StringField('Фамилия', validators=[Optional()])
    username = StringField(
        'Username', validators=[DataRequired(
            message='Это поле обязательно'
        )]
    )
    email = EmailField(
        'Email', validators=[DataRequired(
            message='Это поле обязательно'
        ), Email()]
    ),
    password = PasswordField(
        'Пароль', validators=[DataRequired(
            message='Это поле обязательно'
        )]
    )
    password2 = PasswordField(
        'Повторите пароль', validators=[DataRequired(
            message='Это поле обязательно'
        ), 
        EqualTo(
            fieldname='password', message='Пароли не совпадают'
        )]
    )
    submit = SubmitField('Отправить')
