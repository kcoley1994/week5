from flask_wtf import FlaskForm
from wtforms import StringField, SearchField
from wtforms.validators import DataRequired

class UserSearch(FlaskForm):
    search_pokemon = StringField('Search Pokemon',validators=[DataRequired()])
    search = SearchField()