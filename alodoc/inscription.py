from wtforms import StringField, PasswordField, SubmitField,SelectField,IntegerField
from wtforms.validators import DataRequired, EqualTo, Length, Email
from flask_wtf import FlaskForm

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    nom = StringField('First name ', validators=[DataRequired(), Length(min=4, max=20)])
    prenom = StringField('Last name ', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    genre = SelectField('gender', choices=[('male'),('female')], validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    adresse = StringField('address ', validators=[DataRequired(), Length(min=4, max=20)])
    ville = StringField('city ', validators=[DataRequired(), Length(min=4, max=20)])
    pays = StringField('country ', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Password confirm', validators=[DataRequired(), EqualTo('password')])
    envoyer = SubmitField('Submit')