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
	model_city = Cities.query.order_by(Cities.cityrank).all()

	if form_city.validate_on_submit():
		name_prompt = Cities.query.filter_by(cityname=form_city.city_name.data).first()
		rank_prompt = Cities.query.filter_by(cityrank=form_city.city_rank.data).first()

		if not name_prompt is None:
			flash('Name of city is existence!!!')
		else:
			if rank_prompt is None:
				rank = form_city.city_rank.data
			else:
				rank = Cities.query.count()+1
			name = form_city.city_name.data
			db.create_all()
			c = Cities(name,rank)
			db.session.add(c)
			db.session.commit()

			flash(f'{form_city.city_name.data} is added')

		return redirect('/')		

	return render_template("home.html", title_pass = title_cities, XX = greeting, top_cities = form_city, name_cities = model_city)
