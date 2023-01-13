from app import app
from flask import render_template, request
from .models import User, Deck
from app.forms import UserSearch
import requests, json



@app.route('/')
@app.route('/home' )  
def home():
    form = UserSearch()
    users = User.query.all()
    posts = Deck.query.all()
   
    
    return render_template('index.html',form=form, users=users, posts=posts)    


#methods = ['GET', 'POST']
 # if request.method == 'POST':
    #     if form.validate():
    #         search_pokemon= form.search_pokemon.data
    #         url =f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
    #         response = requests.get(url)
    #         if response.ok == True:
    #             data = response.json()
    #             pokemon_name = data['forms'][0]['name']
    #             pokemon_abilities = data['abilities'][1]['ability']['name']
    #             pokemon_base_exp = data['base_experience']
    #             pokemon_sprite = data['sprites']['front_shiny']
    #             pokemon_attack = data['stats'][1]['base_stat']
    #             pokemon_hp = data['stats'][0]['base_stat']
    #             pokemon_defense = data['stats'][2]['base_stat']

    #         searching = UserSearch(pokemon_name,pokemon_abilities,pokemon_base_exp,pokemon_sprite,pokemon_attack,pokemon_hp,pokemon_defense)
    #     else: 
    #         pass
    # #searching=searching