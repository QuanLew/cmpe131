from myapp import myapp_obj

@myapp_obj.route("/")
def homepage():
	return "Hello"
