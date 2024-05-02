from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, EqualTo, Length, Email
from flask_wtf import FlaskForm

class Docteurform(FlaskForm):
    nom = StringField('Nom ', validators=[DataRequired(), Length(min=4, max=20)])
    prenom = StringField('prenom ', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    genre = SelectField('Sexe', choices=[('male'),('female')], validators=[DataRequired()])
    age = IntegerField('Âge', validators=[DataRequired()])
    adresse = StringField('adresse ', validators=[DataRequired(), Length(min=4, max=20)])
    ville = StringField('ville ', validators=[DataRequired(), Length(min=4, max=20)])
    pays = StringField('pays ', validators=[DataRequired(), Length(min=4, max=20)])
    spe = StringField('specialite ', validators=[DataRequired(), Length(min=4, max=20)])
    submit = SubmitField('Envoyer')