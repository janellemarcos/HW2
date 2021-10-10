import time

def calculate_time(func):
	'''Takes in a function. Returns the function time.'''
	def timed():
		'''Gets the start time, runs the function, gets the end time and prints the total time'''
		start = time.time()
		result = func
		end = time.time()
		funcTime = end - start
		print('Total time ' + str(funcTime))
	return timed
	
'''sleep2 = calculate_time(time.sleep(2))
sleep2()'''
