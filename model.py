"""Models and database functions for carbon and temperature project"""

from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

###########################################
# Model definitions 

class Temperature(db.Model):
	"""Stores temperatures by date"""

	__tablename__ = "temperatures"

	temperature_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	year = db.Column(db.String(4), nullable=False)
	month = db.Column(db.String(3), nullable=False)
	celsius = db.Column(db.String, nullable=True)
	annual_mean_j_d = db.Column(db.String, nullable=True)
	annual_mean_d_n = db.Column(db.String, nullable=True)

class CarbonLevel(db.Model):
	"""Stores carbon dioxide levels by date"""

	__tablename__ = "carbonlevels"

	carbon_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	year = db.Column(db.String, nullable=False)
	month = db.Column(db.String, nullable=False)
	average = db.Column(db.String, nullable=True)
	interpolated = db.Column(db.String, nullable=True)
	season_corr = db.Column(db.String, nullable=True)
	daily = db.Column(db.String, nullable=True)

############################################
# Helper functions

def connect_to_db(app):
	"""Connects the database to our Flask app"""

	app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///warming'
	db.app = app
	db.init_app(app)

if __name__ == "__main__":

	from server import app 
	connect_to_db(app)
	print "Connected to database"

