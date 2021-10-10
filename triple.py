def tripler(func):
	'''Takes in a function. Returns the function three.'''
	def three():
		'''Runs the function three times'''
		func()
		func()
		func()
	return three
	
'''@tripler	
def test():
	print('MOO')
	
if __name__ == "__main__":
	test()'''
