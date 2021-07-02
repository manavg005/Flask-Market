from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class RegisterForm(FlaskForm):
    username=StringField(lable='username')
    email_address=StringField(lable = 'email')
    password1 = PasswordField(lable='password1')
    password2 = PasswordField(lable='password2')
    submit = SubmitField(lable='submit')