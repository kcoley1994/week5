from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class Pokemon(FlaskForm):
    pokemon_name = StringField('Pokemon Name', validators=[DataRequired()])
    pokeball = SubmitField()