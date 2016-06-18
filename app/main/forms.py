from flask.ext.wtf import Form
from wtforms import StringField, SubmitField,SelectField,PasswordField
from wtforms.validators import Required,Email,Length,Regexp,EqualTo


class AgentsForm(Form):
  Name = StringField('Name of property', validators=[Required()])
  Location = StringField('Location', validators=[Required()])
  Price= StringField('Price', validators=[Required()])
  Contact= StringField('Contact', validators=[ Required(), Length(1, 64), Regexp('[0-9]', 0,
 	'phone numbers must have only numbers, ')])
  Category=SelectField('Category',choices=[('Plot','Plot'),('Apartment','Apartment'),('Rentals','Rentals')],validators=[Required()])
  submit = SubmitField('Submit')

class LoginForm(Form):
	email = StringField('Email', validators=[Required(), Length(1, 64),Email()])
	username = StringField('username', validators=[Required()])
	password = PasswordField('Password', validators=[Required()])
	submit = SubmitField('Log In')

class RegistrationForm(Form):
	email = StringField('Email', validators=[Required(), Length(1, 64),Email()])
	username = StringField('Username', validators=[ Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
 	'Usernames must have only letters, ''numbers, dots or underscores')])
 	password = PasswordField('Password', validators=[Required(), EqualTo('password2', message='Passwords must match.')])
 	password2 = PasswordField('Confirm password', validators=[Required()])
 	submit = SubmitField('Register')
 