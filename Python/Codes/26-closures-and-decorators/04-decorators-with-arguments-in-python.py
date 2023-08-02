# Creating decorators with arguments
def greeting_decorator(greeting):
    def my_decorator(func):
        def wrapper_function(*args, kwargs):
            print(greeting)
            result = func(*args, kwargs)
            return result

        return wrapper_function

    return my_decorator
