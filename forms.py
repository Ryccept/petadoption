from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Optional, Email, URL, Length, NumberRange

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField('Pet Name', validators=[InputRequired()])
    species = SelectField('Pet Species', choices=[("cat", "Cat"), ("dog", "Dog"), ("rat", "Rat"), ("lizard", "Lizard")])
    photo_url = StringField('Image URL Link', validators=[Optional(), URL(message='Enter a valid URL Link.')])
    age = IntegerField('Pet Age', validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField('Comments', validators=[Optional(), Length(min=10)])
    available = BooleanField('Available for Adoption?', validators=[Optional()])