from app import app
from flask import render_template

from app.forms import UserSearch



@app.route('/')
@app.route('/home')
def home():
    form = UserSearch()
    
    
    return render_template('index.html',form=form)



