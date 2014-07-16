from flask_wtf import Form
from wtforms import fields
from wtforms.validators import Required, Length, Email

class ContactForm(Form):
    email = fields.StringField('Email', validators=[Required(), Length(1, 64), Email()])
    username = fields.StringField('Username', validators=[Required()])
    button = fields.SubmitField('Register')
    
    def to_model(self, user):
        user.email = self.email.data
        user.username = self.username.data