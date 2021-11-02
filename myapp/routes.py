from myapp import myapp_obj
from flask import render_template

@myapp_obj.route("/")
def homepage():
	title_cities = 'Top Cities'
	greeting = "Quan"
	return render_template("base.html", title_pass = title_cities, XX = greeting)
