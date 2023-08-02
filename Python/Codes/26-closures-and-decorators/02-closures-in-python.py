# Function that returns another function
def square(x):
	def _(y):
		return x * y
	return _

# This function can be used as follows:
square_of_two = square(2)
square_of_two(4)
square_of_three = square(3)
square_of_three(4)