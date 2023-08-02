# This code prints "Hello, Kolledge scholars!!" to the console
print("Hello, Kolledge scholars!!")


# This is a single line comment
print("Hello, Kolledge scholars!!")



'''
This is a Multi-line String literal.
This can be used as a multi-line comment
because Python interpreter ignores any 
multi-line string that is not assigned to a variable.
'''
print("Hello, Kolledge scholars!!")


print("Hello, Kolledge scholars!!")  # This is an inline comment


# Returns a customized message to the scholar
# parameter 1 - scholar_name : Name of the Kolledge scholar
# parameter 2 - msg_type : 1 for simple message, 2 for funky message
# returns - Customized message string
def welcome(scholar_name, msg_type):
    if msg_type == 1:
        msg = "Hello " + scholar_name
    elif msg_type == 2:
        msg = "Howdy " + scholar_name + "!!! Yo."

    return msg



import math
def calc_area(radius):
    """Calculates the area of a circle as per the value of radius param."""
    return math.pi * radius ** 2
