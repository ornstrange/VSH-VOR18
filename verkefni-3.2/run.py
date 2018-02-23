#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from project import app, db
from project.models import User, Post

@app.shell_context_processor
def make_shell_context():
  return {'db': db, 'User': User, 'Post': Post}

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run('0.0.0.0', port=port)
