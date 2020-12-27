from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField

class AddressForm(FlaskForm):
    list = TextAreaField('Address')
    submit = SubmitField("Submit")


