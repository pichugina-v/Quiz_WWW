from flask_wtf import FlaskForm
from wtforms import(
    StringField, PasswordField,
    SubmitField, EmailField
)
from wtforms.validators import (
    Optional, Email,
    DataRequired, EqualTo
)


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Отправить')


class RegistrationForm(FlaskForm):
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
    )
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
