import os
import sqlite3 as sql
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

# basic stuff
app = Flask(__name__)
app.config.from_object(__name__) # config from this file

# config stuff
app.config.update(dict(
  DATABASE=os.path.join(app.root_path, 'flaskr.db'),
  SECRET_KEY = 'prumpirass',
  USERNAME = 'admin',
  PASSWORD = 'admin'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

# ehv db dot
def connect_db():
  # connect to db
  rv = sql.connect(app.config['DATABASE'])
  rv.row_factory = sql.Row
  return rv

def get_db():
  # opens a new db connection if not there
  if not hasattr(g, 'sqlite.db'):
    g.sqlite_db = connect_db()
  return g.sqlite_db

def init_db():
  db = get_db()
  with app.open_resource('schema.sql', mode='r') as f:
    db.cursor().executescript(f.read())
  db.commit()

@app.cli.command('initdb')
def initdb_command():
  # init the db with command
  init_db()
  print("Database initialized!")

@app.teardown_appcontext
def close_db(error):
  # closes db at end of request
  if hasattr(g, 'sqlite.db'):
    g.sqlite_db.close()


# route/view stuff
@app.route('/')
def show_entries():
  db = get_db()
  cur = db.execute('select title, text from entries order by id desc')
  entries = cur.fetchall()
  return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
  if not session.get('logged_in'):
    abort(401)
  db = get_db()
  db.execute('insert into entries (title, text) values (?, ?)',
             [request.form['title'], request.form['text']])
  db.commit()
  flash('New entry was successfully posted!')
  return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
  error = None
  if request.method == 'POST':
    if request.form['username'] != app.config['USERNAME']:
      error = 'Invalid username'
    elif request.form['password'] != app.config['PASSWORD']:
      error = 'Invalid password'
    else:
      session['logged_in'] = True
      flash('You were logged in')
      return redirect(url_for('show_entries'))
  return render_template('login.html', error=error)

@route('/logout')
def logout():
  session.pop('logged_in', None)
  flash('You were logged out, you whore')
  return redirect(url_for('show_entries'))
