def multiply():

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
	
	took size from user
	then a loop = size
	get input values from user
	if input is valid, put them in list and multiply together
	else return False (invalid value)
	
	"""

	num = input ("Enter number of elements : ")
	myList = []
	result = 1

	for n in range(int(num)):
		val = input ("Enter value : ")
		if val.isdigit() == True:
			myList.append(int(val))
			result *= myList[n]
		else:
			print("Invalid value!!!")
			return False
	print(f"Input = {myList}")
	#print(f"Output = {result}")
	return (f"Output = {result}")
