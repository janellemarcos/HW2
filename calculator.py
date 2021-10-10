def calculator(num1, num2, operator):
	'''Takes in two numbers (num1 and num2) and the operation. Returns the calculation.
	Returns False if the operation was invalid.'''
	if operator == '+':
		return float(num1) + float(num2)
	elif operator == '-':
		return float(num1) - float(num2)
	elif operator == '*':
		return float(num1) * float(num2)
	elif operator == '/':
		return float(num1) / float(num2)
	elif operator == '//':
		return float(num1) // float(num2)
	elif operator == '**':
		return float(num1) ** float(num2)
	else:
		return False


def parse_input():
	'''Takes the user's equation, parses the input, calls the calculator function and prints the result.'''
	equation = str(raw_input("Enter equation: "))
	list = equation.split()
	number1 = list[0]
	number2 = list[2]
	optr = list[1]
	result = calculator(number1, number2, optr)
	print(result)
