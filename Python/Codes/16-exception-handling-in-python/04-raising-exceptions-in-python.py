# Manually raising Exceptions in Python
def show_details(name, id):
    try:
        print("Inside try block")
        if id < 0:
            raise Exception("Id should be a Positive number.")
        else:
            print(f"The name is : {name}")
            print(f"The id is : {id}")
    except Exception as e:
        print("Inside except block : ", e)


show_details("John", -5)
print()
show_details("Alice", 1)





# Using Exception classes while raising exception
def divide(numerator, denominator):
    try:
        print("Inside try block")
        if denominator == 0:
            raise ZeroDivisionError("Sorry, Denominator cannot be zero.")
        else:
            d = numerator / denominator
            print(f"The value of quotient is {d}")
    except ZeroDivisionError as e:
        print("Inside except block : ", e)


divide(20, 0)
print()
divide("20", 4)
