from flask import render_template, flash, redirect, url_for
from project import app

@app.route('/')
def index():
  return render_template('index.html', title='Jaws')

@app.route('/actors')
def actors():
  return render_template('actors.html', title='Leikarar')

@app.route('/contact')
def contact():
  return render_template('contact.html', title='Hafa Samband')
