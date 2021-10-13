import time 

def calculate_time(function):
	def wrapper():
		start = time.time()
		function()
		end = time.time()
		total = end - start	
		print(f'Total time {total}')
	return wrapper

def sayHi():
	time.sleep(2)

sayHi_v2 = calculate_time(sayHi)

sayHi_v2()
