from myapp import myapp_obj
from flask import render_template
from myapp import db
from myapp.models import Cities
from myapp.forms import TopCities

@myapp_obj.route("/", methods = ['GET','POST'])
def homepage():
	title_cities = 'Top Cities'
	greeting = "Quan"
	form_city = TopCities()
	model_city = Cities.query.all()
	return render_template("home.html", title_pass = title_cities, XX = greeting, top_cities = form_city, name_cities = model_city)
