from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, EqualTo, Length, Email
from flask_wtf import FlaskForm

class Docteurform(FlaskForm):
    nom = StringField('First name ', validators=[DataRequired(), Length(min=4, max=20)])
    prenom = StringField('Last name ', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    genre = SelectField('gender', choices=[('male'),('female')], validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    adresse = StringField('address ', validators=[DataRequired(), Length(min=4, max=20)])
    ville = StringField('city ', validators=[DataRequired(), Length(min=4, max=20)])
    pays = StringField('country ', validators=[DataRequired(), Length(min=4, max=20)])
    spe = StringField('speciality ', validators=[DataRequired(), Length(min=4, max=20)])
    submit = SubmitField('Submit')