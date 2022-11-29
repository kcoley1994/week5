from app import app
from flask import render_template

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/fav_five')
def fav_five():
    favorites = ['J Cole', 'Dwayne Wade', 'Kobe Bryant', 'Lebron James', 'Call of Duty: Warzone']
    return render_template("favorite.html", names= favorites)