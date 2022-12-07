from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key =True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False, unique= True)
    email = db.Column(db.String(250), nullable=False, unique= True)
    password = db.Column(db.String(250), nullable=False)
    post = db.relationship('Post', backref='author', lazy=True)
    deck =db.relationship('Deck',backref='author', lazy=True )

    def __init__(self, first_name, last_name, username, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

class Post(db.Model):
    id =  db.Column(db.Integer, primary_key =True)
    title = db.Column(db.String(50), nullable=False)
    img_url = db.Column(db.String, nullable=False)
    caption = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, title, img_url, caption, user_id):
        self.title = title
        self.img_url = img_url
        self.caption = caption
        self.user_id = user_id
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def update_db(self):
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


class Deck(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(50), nullable=False)
    pokemon_abilities = db.Column(db.String(50), nullable=False)
    pokemon_base_exp = db.Column(db.Integer, nullable=False)
    pokemon_sprite = db.Column(db.String, nullable=False)
    pokemon_attack = db.Column(db.Integer, nullable=False)
    pokemon_hp = db.Column(db.Integer, nullable=False)
    pokemon_defense = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, name, pokemon_abilities, pokemon_base_exp, pokemon_sprite, pokemon_attack, pokemon_hp, pokemon_defense, user_id):
        self.name = name
        self.pokemon_abilities = pokemon_abilities
        self.pokemon_base_exp = pokemon_base_exp
        self.pokemon_sprite = pokemon_sprite
        self.pokemon_attack = pokemon_attack
        self.pokemon_hp = pokemon_hp
        self.pokemon_defense = pokemon_defense
        self.user_id= user_id


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()