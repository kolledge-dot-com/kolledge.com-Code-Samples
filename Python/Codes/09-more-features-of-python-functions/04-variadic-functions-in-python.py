def my_func(a, b, *c):
    print("a = ", a)
    print("b = ", b)
    print("c = ", c)


my_func(10, 20, 30, 40, 50)


# Variadic Parameter - *args
def my_func(a, b, *args):
    print("Value of a = ", a)
    print("Value of b = ", b)
    print("Value of arg_1 = ", args[0])
    print("Value of arg_2 = ", args[1])
    print("Value of arg_3 = ", args[2])
    print()

    print("Iterating over args")
    # using for loop
    for arg in args:
        print(arg)


my_func(10, 20, 30, 40, 50)