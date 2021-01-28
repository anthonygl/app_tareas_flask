from wtforms import Form

#se convertira en un input tipo texto y input tipo password
from wtforms import StringField, PasswordField

class LoginForm(Form):
    username = StringField('Username')
    password= PasswordField('Password')