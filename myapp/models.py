from myapp import db

class Cities(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	cityname = db.Column(db.String(64), unique = True, index = True)
	cityrank = db.Column(db.Integer, unique = True)

	def set_rank(self,cityrank):
		self.cityrank = cityrank

	def __repr__(self):
                return f'{self.cityname}'
