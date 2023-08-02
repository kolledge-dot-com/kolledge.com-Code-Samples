# Docstrings in Python
def my_func():
    '''This is the docstring for function my_func.
    We can use triple or double quotes to create docstrings.
    docstrings are stored in the __doc__ property of the function.
    docstrings of any function are used by
    help function as documentation of that function'''

    pass


print("printing docstring using __doc__:")
print(my_func.__doc__)

print()
print("printing docstring Using help:")
help(my_func)