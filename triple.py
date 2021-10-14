def tripler(function):
	"""
	create a decorator to run a function

	Parameter
	--------

	return a function nested another function
	call the function 3 times
	"""	
	def wrapper():
		function()
		function()
		function()
	return wrapper

@tripler
def say_hi():
	print("hello")

#say_hi()
