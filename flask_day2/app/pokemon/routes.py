from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from .forms import Pokemon
from app.models import Deck
import requests, json

pokemon = Blueprint('pokemon', __name__, template_folder='pokemon_templates')

@pokemon.route('/wild_pokemon', methods=['GET', 'POST'])
@login_required
def pokedex():
    form = Pokemon()
    if request.method == 'POST':
        if form.validate():
            pokemon_name= form.pokemon_name.data
            url =f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
            response = requests.get(url)
            if response.ok == True:
                data = response.json()
                pokemon_name = data['forms'][0]['name']
                pokemon_abilities = data['abilities'][1]['ability']['name']
                pokemon_base_exp = data['base_experience']
                pokemon_sprite = data['sprites']['front_shiny']
                pokemon_attack = data['stats'][1]['base_stat']
                pokemon_hp = data['stats'][0]['base_stat']
                pokemon_defense = data['stats'][2]['base_stat']

        post = Deck(pokemon_name,pokemon_abilities,pokemon_base_exp,pokemon_sprite,pokemon_attack, pokemon_hp,pokemon_defense,current_user.id)
        
        post.save_to_db()


        return redirect(url_for('pokemon.my_pokemon'))
    return render_template('catch_pokemons.html', form=form)

@pokemon.route('/my_pokemons')
@login_required
def my_pokemon():
    posts = Deck.query.all()
    
    return render_template('view_pokemons.html', posts=posts[::-1])

        