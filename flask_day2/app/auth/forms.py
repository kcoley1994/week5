from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class UserCreationForm(FlaskForm):
    choose_your_pokemon = StringField('Choose Your Pokemon', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    sign_up = SubmitField()