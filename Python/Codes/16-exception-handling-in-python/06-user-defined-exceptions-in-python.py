# Code Sample for user defined exceptions
class MyException(Exception):
    def __init__(self, msg):
        self.msg = msg


def show_details(name, id):
    try:
        print("Inside try block")
        if id < 0:
            raise MyException
        else:
            print(f"The name is : {name}")
            print(f"The id is : {id}")
    except MyException as e:
        print("Inside MyException except block : ", e)


show_details("John", -5)
print()
show_details("Alice", 1)






# Catching multiple user-defined exception
class MyException(Exception):
    def __init__(self, msg):
        self.msg = msg


class MySecondException(Exception):
    def __init__(self, msg):
        self.msg = msg

def show_details(name, id):
    try:
        print("Inside try block")
        if id < 0:
            raise MyException("MyException : Id should be a Positive number.")
        elif id > 1000:
            raise MySecondException("MySecondException : Id cannot be greater than 1000.")
        else:
            print(f"The name is : {name}")
            print(f"The id is : {id}")
    except (MyException, MySecondException) as e:
        print(e)


show_details("John", -5)
print()
show_details("Alice", 2000)







# Getting type of user-defined exception
class MyException(Exception):
    def __init__(self, msg):
        self.msg = msg


class MySecondException(Exception):
    def __init__(self, msg):
        self.msg = msg

def show_details(name, id):
    try:
        print("Inside try block")
        if id < 0:
            raise MyException("Id should be a Positive number.")
        elif id > 1000:
            raise MySecondException("Id cannot be greater than 1000.")
        else:
            print(f"The name is : {name}")
            print(f"The id is : {id}")
    except (MyException, MySecondException) as e:
        type_excep = type(e)
        print(e)
        print (f"Type of Exception : {type_excep}")


show_details("John", -5)
print()
show_details("Alice", 2000)