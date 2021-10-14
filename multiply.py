def multiply_list(list):

	"""

	Multiply each element from myList
	
	Parameter
	--------
	number : string
	       hold input from user's prompt
	myList : array of integer
	       list contain input from user
	result : int
	       get result from multiplying whole list
	
	if each element in list is valid, put them in list and multiply
	else any element is invalid, immediately return False (invalid value)
	
	"""

	result = 1

	for n in list:
		if type(n) == int or type(n) == float:
			result *= n
		else:
			print("Invalid value!!!")
			return False
	print(f"Input = {list}")
	return (f"Output = {result}")

print(multiply_list([1,3,4,5]))
