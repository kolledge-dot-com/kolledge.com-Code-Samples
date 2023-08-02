# Code Sample for try…except block
def my_function(x, y):
    print("Inside my_function")

    z = (x * y)/ (x + y)

    print("Value of z = ", z)



my_function(10, -10)



def my_function(x, y):
    print("Inside my_function")
    try:
        print("Inside try block")
        z = (x * y)/ (x + y)
        print("Value of z = ", z)
    except Exception as e:
        print()
        print("Inside except block")
        print("An exception has occurred")
        print("Terminating the program execution gracefully.")



my_function(10, -10)




# Catching specific exceptions
def my_function(x, y):
    print("Inside my_function")
    try:
        print("Inside try block")
        z = (x * y)/ (x + y)
        print("Value of z = ", z)
    except ZeroDivisionError as e:
        print("Inside except block : ", e)


my_function(10, -10)




# Catching Multiple Exceptions
def my_function(x, y, string):
    print("Inside my_function")
    try:
        print("Inside try block")
        z = (x * y) / (x + y)
        print("Value of z = ", z)

        index = string[10]
        print("Character at index 10 : ", index)
    except TypeError as te:
        print("Inside TypeError except block : ")
        print(te)
    except ZeroDivisionError as ze:
        print("Inside ZeroDivisionError except block : ")
        print(ze)
    except Exception as e :
        print("Inside generic Exception except block : ")
        print(e)


my_function("10", -10, "Hello")
print()
my_function(5,-5, "Hello")
print()
my_function(4, 1, "Hello")






# Grouping Exceptions in Python
def my_function(x, y):
    print("Inside my_function")
    try:
        print("Inside try block")
        z = (x * y) / (x + y)
        print("Value of z = ", z)
    except (TypeError, ZeroDivisionError) as e:
        print("Inside Group except block : ")
        print(e)
        print("Please check the input data")
    except Exception as e:
        print("Inside generic Exception except block : ")
        print(e)


my_function("10", -10)
print()
my_function(5, -5)