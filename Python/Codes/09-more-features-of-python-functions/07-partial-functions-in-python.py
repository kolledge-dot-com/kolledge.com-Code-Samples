from functools import partial

# Partial Functions in Python
def my_func(a, b, c, d):
    print("Value of a = ", a)
    print("Value of b = ", b)
    print("Value of c = ", c)
    print("Value of d = ", d)


partial_my_func = partial(my_func,10,20,30)
partial_my_func(100)



# using *args with partial functions
def my_func(a, b, *args):
    print("Value of a = ", a)
    print("Value of b = ", b)
    print("Value of args = ", args)


partial_my_func = partial(my_func,10,20,30,40,50)
partial_my_func()



# Using **kwargs with partial functions
def my_func(a, b, **kwargs):
    print("Value of a = ", a)
    print("Value of b = ", b)
    print("Value of kwargs = ", kwargs)


partial_my_func = partial(my_func,10,20,first=40,second=50)
partial_my_func()