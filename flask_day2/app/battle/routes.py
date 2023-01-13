from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import User, Deck
from flask_login import current_user, login_required
from app.forms import UserSearch

battle = Blueprint('battle', __name__,template_folder ='battle_templates')

@battle.route('/battle')
@login_required
def choose_opponent():
    form = UserSearch()
    users = User.query.all()
    posts = Deck.query.all()
    
    return render_template('battle.html',form=form,users=users, posts=posts)

@battle.route('/vs<int:id>')
def opponent(id):
    posts = User.query.get(id)
    decks =Deck.query.get(id)
    my =Deck.query.all()
    if posts:
        return render_template('battle2.html',posts=posts, decks=decks, my = my)
    else:
        return redirect(url_for('battle.battle.html'))
        
