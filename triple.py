def tripler(function):
	def wrapper():
		function()
		function()
		function()
	return wrapper

@tripler
def say_hi():
	print("hello")

say_hi()
