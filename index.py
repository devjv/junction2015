from flask import Flask, render_template
from flask.ext.social.datastore import SQLAlchemyConnectionDatastore
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SOCIAL_FACEBOOK'] = {
	'consumer_key': '1644291215859316',
	'consumer_secret': 'ead6688f2f79b9d7c0478e950d227f2a'
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True)
	email = db.Column(db.String(120), unique=True)

	def __init__(self, username, email):
		self.username = username
		self.email = email

class Airport(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	code = db.Column(db.String(5))

class Flight(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	destination_airport = Airport
	departure_airport = Airport
	departure_time = db.Column(db.Date)
	code = db.Column(db.String(255))

class Offer(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	flights = list flights
	money = db.Column(db.Integer)

if __name__ == '__main__':
	app.run(debug=True)
