from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand



basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)
migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)


class Properties(db.Model):
	__tablename__ = 'properties'
	id = db.Column(db.Integer, primary_key=True)
	name= db.Column(db.String(64), unique=True)
	location= db.Column(db.String(64))
	Price= db.Column(db.String(64))
	Category= db.Column(db.String(64))
	Contact= db.Column(db.String(64))
	def __repr__(self):
		return '<properties %r>' %(self.name,self.location,self.Price,self.Category)


class User(db.Model):
	"""An admin user capable of viewing reports.

	:param str email: email address of user
	:param str password: encrypted password for the user

	"""
	__tablename__ = 'user'

	email = db.Column(db.String, primary_key=True)
	username = db.Column(db.String)
	password = db.Column(db.String)
	authenticated = db.Column(db.Boolean, default=False)

	def is_active(self):
		"""True, as all users are active."""
		return True

	def get_id(self):
		"""Return the email address to satisfy Flask-Login's requirements."""
		return self.username

	def is_authenticated(self,password):
		"""Return True if the user is authenticated."""
		return self.authenticated

	def is_anonymous(self):
		"""False, as anonymous users aren't supported."""
		return False

	def __repr__(self):
		return '<users %r>' %(self.username,self.email,self.password)
 

if __name__ == '__main__':
	manager.run()
































	