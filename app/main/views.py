
from flask import Flask,render_template,redirect,url_for,flash,session
from flask.ext.wtf import Form
from flask import request
from flask.ext.bootstrap import Bootstrap
from forms import AgentsForm
from forms import LoginForm
from forms import RegistrationForm
from models import User,Properties,db
from flask.ext.login import login_user, logout_user, login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)


#agents form
@app.route('/agents', methods=['GET', 'POST'])
def agents():
	form =AgentsForm(request.form)
	if request.method == 'GET':	
		return render_template('agents.html', form=form)

		
	if request.method == 'POST':
		if form.validate_on_submit():
			properties= Properties(name=form.Name.data,
					location=form.Location.data,
					Price=form.Price.data,
					Category=form.Category.data,
					Contact=form.Contact.data,)
		form.populate_obj(properties)
		db.session.add(properties)
		try:
			db.session.commit()
		except IntegrityError:
			db.session.rollback()
		flash ('you have successfully submitted your form')	
	return render_template('index.html',form=form)



# registration form
@app.route('/signup', methods=['GET', 'POST'])
def  register():
	form=RegistrationForm(request.form)
	if request.method == 'GET':	
		return render_template('register.html', form=form)
	
	if request.method == 'POST':
		def validate_email(self, field):
			if User.query.filter_by(email=field.data).first():
				raise ValidationError('Email already registered.')
		def validate_username(self, field):
			if User.query.filter_by(email=field.data).first():
				raise ValidationError('Username already in use.')

		user= User(username=form.username.data,email=form.email.data,password=form.password.data)
		form.populate_obj(user)
		db.session.add(user)
		db.session.commit()
		db.session.flush()
	return redirect(url_for('index'))
	flash ('your registration was successfull')
	

def load_user(user_id):
	return User.query.get(int(user_id))

#login form
@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user is not None and user.is_authenticated(form.password.data):
			login_user(user, form.remember_me.data)
			return redirect(request.args.get('next') or url_for('index'))
		flash('Invalid email or password.')
		return redirect(url_for('index'))
	else:
		return render_template('login.html', form=form, title="Login")

@app.route('/logout')
@login_required
def logout():
	logout_user()
	flash('You have successfully been logged out.')
	return redirect(url_for('index'))
		

	
 
@app.route('/index')
def index():
	return render_template('index.html')


@app.route('/plots')
def plots():
	plots = Properties.query.filter_by(Category='Plot').all()
	return render_template('plots.html', plots=plots)


@app.route('/apartments')
def apartment():
	apartments= Properties.query.filter_by(Category='Apartment').all()
	return render_template('apartments.html', apartments=apartments)


@app.route('/residential')
def rentals():
	rentals = Properties.query.filter_by(Category='Rentals').all()
	return render_template('residential.html', rentals=rentals)	

	


if __name__ == '__main__':
	app.run(debug=True,port=5001)	