from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key =True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False, unique= True)
    email = db.Column(db.String(250), nullable=False, unique= True)
    password = db.Column(db.String(250), nullable=False)
    post = db.relationship('Post', backref='Author', lazy=True)

    def __init__(self, first_name, last_name, username, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password

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
        


# class Login(db.Model):
#     id = db.Column(db.Integer, primary_key =True)
#     user_name = 
#     password =