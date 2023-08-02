# Python decorator example :
def hello_decorator(func):
    def inner():
        print("Hello, world!")
        func()

    return inner


@hello_decorator
def hello():
    print("Greetings from the decorated function.")


hello()
