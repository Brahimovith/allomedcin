from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import enum

from .view import app

# Créez une instance de SQLAlchemy et liez-la à votre application Flask (app):
db = SQLAlchemy(app)

class Gender(enum.Enum):
    female = 0
    male = 1
    

class client(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
   # first_name = db.Column(db.String(100), nullable=False)
    #last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    #gender = db.Column(db.Enum(Gender), nullable=False)  # Peut être 'Male', 'Female', 'Other'
    #age = db.Column(db.Integer, nullable=False)
    #address = db.Column(db.String(255), nullable=False)
    #city = db.Column(db.String(100), nullable=False)
    #country = db.Column(db.String(100), nullable=False)

    def check_password(self,mdp):
        if (self.password == mdp):
            return True
        else:
            return False



class doctorvalide(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.Enum(Gender), nullable=False)  # Peut être 'Male', 'Female', 'Other'
    age = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    specialite = db.Column(db.String(100), nullable=False)

class doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.Enum(Gender), nullable=False)  # Peut être 'Male', 'Female', 'Other'
    age = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    specialite = db.Column(db.String(100), nullable=False)


with app.app_context():
    db.create_all()