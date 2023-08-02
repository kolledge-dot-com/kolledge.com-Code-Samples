# Accessing a Global Variable

glb = "I am Global."

def my_func():
	print("Accessing global from inside : ", glb)

my_func()


# Modifying global variable without using global keyword
glb = "I am Global"

def my_func():
	glb = "I am local"
	print("Accessing global from inside : ", glb)

my_func()
print("Accessing global from outside : ", glb)



# Modifying global variable using global keyword

glb = "I am Global"

def my_func():
	global glb
	glb = "I am local"
	print("Accessing global from inside : ", glb)

my_func()
print("Accessing global from outside : ", glb)