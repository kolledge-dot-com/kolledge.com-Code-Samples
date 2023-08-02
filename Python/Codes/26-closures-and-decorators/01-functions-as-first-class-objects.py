# Passing functions as arguments of other functions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# our own function
def is_even(num):
	return num % 2 == 0

# using the built-in filter function
filtered_numbers = filter(is_even, numbers)

print(list(filtered_numbers))




# Assigning to variables
def greet(name):
	print("Hello, {}!".format(name))

greet("Jill")

# Hello, Jill!

# assigning the function to a variable
greeter = greet("Jack")




# sing attributes of functions
def greet(name):
	print("Hello, {}!".format(name))

print(greet.__name__)