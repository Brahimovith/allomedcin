from flask import Flask
from .view import app

#importez le module models depuis le même répertoire 
#que celui où se trouve le fichier dans lequel vous écrivez ce code
from . import models

# Connect sqlalchemy to app
#models.db.init_app(app)
   