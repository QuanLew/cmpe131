from __future__ import division

def calculator(number1, number2, operator):

	"""
	Do the calculate between two numbers
	
	Parameter
	--------
	num1 : float
	     hold the 1st operation
	num2 : float
	     hold the 2nd operation
	operator : string
	     hold the symbol of operator	

	parse two number to float
        return false if the operator is not existence
	return result if operator is valid
	"""

	result = 0
	
	if type(number1) == int or float and type(number2) == int or float and operator in ('+','-','*','/','//','**'):
		try:
			num1 = float(number1)
			num2 = float(number2)
			if operator == '+':	
				result= num1 + num2	 
			elif operator == '-':	
				result= num1 - num2	 	
			elif operator == '*':	
				result= num1 * num2	 	
			elif operator == '/':	
				result= num1 / num2	 	
			elif operator == '//':	
				result= num1 // num2	 	
			elif operator == '**':	
				result= num1 ** num2
		except ZeroDivisionError:
			print("Can not divide by Zero")
			return False
		
		return result	 		
	else:
		print('Invalid value/operator!!!')
		return False

def parse_input():
	"""
	take the input from user and handle them
	
	parameter
	--------
	prompt : string
	       get input from user
	text : string
	       hold string from split
	num1 : string
	       contain 1st number
	num2 : string
	       contain 2nd number	
	operator : string
	       contain 1 

	get input from user
	split the input by a delimter that is space
	check user'input
	pass these values which just split to the calculator function with 3 parameters
	"""

	prompt = eval("input('Enter equation: ')")
	text = prompt.split(' ')
	if len(text) == 3:
		num1 = text[0]
		num2 = text[2]
		operator = text[1]
	else:
		print('Not valid!')
		exit() 	
	return calculator(num1,num2,operator)

