from flask import Blueprint, render_template

from app.auth.forms import UserCreationForm

import requests

auth = Blueprint('auth',__name__, template_folder='auth_templates')


@auth.route('/signup')
def signup():
    form = UserCreationForm()
    #  def pokemons_info(name):
    #     url =f'https://pokeapi.co/api/v2/pokemon/{name}'
    #     response = requests.get(url)
    #     data= response.json()
    #     new_pokemon_data = []    
    #     pokemon_dict= {}
    #     pokemon_name = data['forms'][0]['name']
    #     pokemon_key = pokemon_name
   
    #     pokemon_dict[pokemon_key] = {
    #     'pokeman_abilities': data['abilities'][1]['ability']['name'],
    #     'pokeman_base_exp' : data['base_experience'],
    #     'pokeman_sprite' : data['sprites']['front_shiny'],
    #     'pokeman_attack' : data['stats'][1]['base_stat'],
    #     'pokeman_hp' : data['stats'][0]['base_stat'],
    #     'pokeman_defense' : data['stats'][2]['base_stat']
    # }
    #     new_pokemon_data.append(pokemon_dict)
    #     return new_pokemon_data
    #     pokemons_info("charizard")

    return render_template('signup.html',form=form)

@auth.route('/login')
def pokemon():
    
    return render_template('pokemon-trainer.html')