import os
SECRET_KEY = '#d#JCqTTW\nilK\\7m\x0bp#\tj~#H'

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')