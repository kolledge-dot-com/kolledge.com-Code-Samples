# try..except..finally construct in Python
def my_function(x, y):
    try:
        print("Inside try block")
        z = (x * y) / (x + y)
        print("Value of z = ", z)
    except Exception as e:
        print("Inside except block : ", e)
    finally:
        print("Inside Finally block")



my_function(5, -5)
print()
my_function(4, 1)






# using finally block without except block
def my_function(x, y):
    try:
        print("Inside try block")
        z = (x * y) / (x + y)
        print("Value of z = ", z)
    finally:
        print("Inside Finally block")



my_function(5, -5)



