from wtforms import SubmitField,SelectField,DateField
from wtforms.validators import DataRequired, EqualTo, Length, Email
from flask_wtf import FlaskForm

class Rendezvous(FlaskForm):
    i=SelectField('select an id',validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d %H:%M', validators=[DataRequired()])
    envoyer = SubmitField('confirm')