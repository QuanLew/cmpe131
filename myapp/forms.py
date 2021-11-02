from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SubmitField
from wtforms.validators import DataRequired, InputRequired

class TopCities(FlaskForm):
	city_name = StringField("City Name", validators = [DataRequired()])
	city_rank = IntegerField("City Rank", validators = [InputRequired()])
	is_visited = BooleanField("Visited")
	submit_form = SubmitField("Submit")
