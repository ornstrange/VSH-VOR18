from project import app
from project.models import *
from flask import render_template

@app.route("/")
def index():
  return "Root Dude"
