def multiply_list(myList):
	'''Takes in a list myList, multiplies elements in the list and returns the product
	Returns False if any item in the list is invalid'''
	result = 1
	for x in myList:
		if type(x) is not int:
			if type(x) is not float:
				return False
		result = result * x
	return result

