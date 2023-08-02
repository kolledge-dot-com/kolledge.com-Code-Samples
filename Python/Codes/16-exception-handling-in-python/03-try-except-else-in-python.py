# Control flow of try...except...else statement
def my_function(x, y):
    try:
        print("Inside try block")
        z = (x * y) / (x + y)
        print("Value of z = ", z)
    except Exception as e:
        print("Inside except block : ", e)
    else:
        print("Inside else block")
    finally:
        print("Inside Finally block")



my_function(5, -5)
print()
my_function(4, 1)