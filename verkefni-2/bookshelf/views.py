from bookshelf import app
from bookshelf.models import booklist
from flask import render_template

@app.route("/")
def index():
  return render_template('index.html', booklist=booklist)

@app.route("/book/<book_name>")
def book(book_name):
  book = list(filter(lambda x: x.name == book_name, booklist))[0]
  return render_template('book.html', book=book)
