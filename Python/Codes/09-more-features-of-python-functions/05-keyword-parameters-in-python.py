def my_func(a, b, **kwargs):
    print("Value of a = ", a)
    print("Value of b = ", b)
    print("Value of kwargs = ", kwargs)
    print()

    print("Iterating over kwargs")
    # using for loop
    for key in kwargs.keys():
        print(key,kwargs[key])


# Calling my_func
d = {"first": 30, "second": 40, "third": 50}
my_func(10, 20, **d)
