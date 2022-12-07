from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from .forms import PostForm
from app.models import Post

trainer=Blueprint('trainer', __name__, template_folder= 'trainer_templates')

@trainer.route('/post/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = PostForm()
    if request.method =='POST':
        if form.validate():
            title = form.title.data
            img_url = form.img_url.data
            caption = form.caption.data

            # print(pokemon, img_url,caption)
            post = Post(title, img_url, caption, current_user.id)

            post.save_to_db()

            return redirect(url_for('trainer.view_posts'))
    return render_template('pokemon_post.html', form=form)

@trainer.route('/posts')
def view_posts():
    posts = Post.query.all()

    return render_template('pokemon_world.html', posts = posts[::-1])

#dynamic routes
@trainer.route('/posts/<int:post_id>')
def view_single_post(post_id):
    post = Post.query.get(post_id)
    if post:     
       return render_template('single_post.html', post=post)
    else:
        return redirect(url_for('trainer.view_posts'))

@trainer.route('/posts/update/<int:post_id>', methods=['GET','POST'])
def update_post(post_id):
    form = PostForm()
    post = Post.query.get(post_id)
    if current_user.id == post.user_id:
        if request.method =='POST':
            if form.validate():
                title = form.title.data
                img_url = form.img_url.data
                caption = form.caption.data


                post.title = title
                post.img_url = img_url
                post.caption = caption

                post.update_db()

                return redirect(url_for('trainer.view_posts'))
    else:
        flash('Unauthorized Location','danger')
        return redirect(url_for('trainer.view_posts'))
    return render_template('update_post.html', form=form, post=post)

@trainer.route('/posts/delete/<int:post_id>')
def delete_post(post_id):
    post = Post.query.get(post_id)
    if post:
       post.delete_from_db()
    return redirect(url_for('trainer.view_posts'))