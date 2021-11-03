from myapp import myapp_obj
from flask import flash,render_template, redirect
from myapp import db
from myapp.models import Cities
from myapp.forms import TopCities

@myapp_obj.route("/", methods = ['GET','POST'])
def homepage():
	title_cities = 'Top Cities'
	greeting = "Quan"
	form_city = TopCities()
	model_city = Cities.query.all()

	if form_city.validate_on_submit():
		#name = Cities.query.filter_by(cityname = form_city.city_name.data).first()
		name = form_city.city_name.data
		rank = form_city.city_rank.data

		if name is None:
			flash('Invalid input!!!')
		else:
			flash(f'{form_city.city_name.data} is added')
			db.create_all()		
			city = Cities(name,rank)
			#city.set_name(name)
			#city.set_rank(rank)
			db.session.add(city)
			db.session.commit()	
		return redirect('/')
	
	return render_template("home.html", title_pass = title_cities, XX = greeting, top_cities = form_city, name_cities = model_city)
