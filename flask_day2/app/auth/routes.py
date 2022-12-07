from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from app.auth.forms import UserCreationForm, UserLoginForm
from app.models import User
from werkzeug.security import check_password_hash


auth = Blueprint('auth',__name__, template_folder='auth_templates')


@auth.route('/signup', methods=['GET','POST'])
def signup():
    form = UserCreationForm()
    if request.method == 'POST':
        if form.validate():
            first_name = form.first_name.data
            last_name = form.last_name.data
            username = form.username.data
            email = form.email.data
            password = form.password.data

            flash('Sign up Complete', 'success')
            user = User(first_name, last_name, username, email, password)
            
            user.save_to_db()
            return redirect(url_for('auth.login'))

    return render_template('signup.html',form=form)

@auth.route('/login', methods=['GET','POST'])
def login():
    form = UserLoginForm()
    if request.method == 'POST':
        if form.validate():
            username = form.username.data
            password = form.password.data
            
            user = User.query.filter_by(username=username).first()
            
            if user:
                if check_password_hash(user.password, password):
                    login_user(user)
                    flash('Successfully Logged in', 'success')
                    return redirect(url_for('trainer.view_posts'))
                else:
                    flash('Invalid Password','danger')
            else:
                flash('User does not exist', 'danger')
    
    return render_template('login.html', form=form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))