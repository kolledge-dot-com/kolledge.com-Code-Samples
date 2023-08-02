# Creating global variables in Python

def my_func():
    print("Accessing global variable from inside : ", glb)


# This is the Global space
glb = "I am global."
print("Accessing global variable from outside : ", glb)
my_func()


# Creating local variables in Python
def my_func():
    lcl = "I am local."
    print("Accessing local variable from inside : ", lcl)


# This is the Global space
my_func()


# Using local variables outside a function
def my_func():
    lcl = "I am local."
    print("Accessing local variable from inside : ", lcl)


# This is the Global space
my_func()
print("Accessing local variable from outside : ", lcl)
