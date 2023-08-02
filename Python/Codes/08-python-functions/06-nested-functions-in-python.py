# Nested Functions in Python
def outer_function():
    print("Inside outer function")

    def inner_function():
        print("Inside inner function")

    inner_function()


outer_function()


# Returning Nested functions from another function
def outer_function():
    print("Inside outer function")

    def inner_function():
        print("Inside inner function")

    return inner_function


f = outer_function()
f()
