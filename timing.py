import time 

def calculate_time(function):
	"""
	Estimate how long the function run

	Parameter
	--------
	start: float
	     hold the beginning time 
	end:   float
	     hold the finishing time
	total: float
	     hold the result of measuring after calling function done

	return a function nested in function
	init time and call function
	measure the time by end - start
	"""
	def wrapper():
		start = time.time()
		function()
		end = time.time()
		total = end - start	
		print(f'Total time {total}')
	return wrapper

def sayHi():
	time.sleep(2)

#sayHi_v2 = calculate_time(sayHi)

##sayHi_v2()
