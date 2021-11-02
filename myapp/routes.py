from myapp import myapp_obj
from flask import render_template
from myapp.forms import TopCities

@myapp_obj.route("/")
def homepage():
	title_cities = 'Top Cities'
	greeting = "Quan"
	cities = TopCities()
	return render_template("home.html", title_pass = title_cities, XX = greeting, top_cities = cities)
