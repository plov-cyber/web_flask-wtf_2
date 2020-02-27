from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    astro_id = StringField('Id астронавта', validators=[DataRequired()])
    astro_pswd = PasswordField('Пароль астронавта', validators=[DataRequired()])
    cap_id = StringField('Id капитана', validators=[DataRequired()])
    cap_pswd = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')
