from flask import render_template, flash, redirect, url_for
from project import app
from project.forms import LoginForm
from project.models import User, Post

@app.route('/')
def index():
  posts = Post.query.all()
  return render_template('index.html', title='Home', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
    return redirect(url_for('index'))
  return render_template('login.html', title='Sign In', form=form)
