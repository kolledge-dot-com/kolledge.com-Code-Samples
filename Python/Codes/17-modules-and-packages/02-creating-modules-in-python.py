# Code sample of creating a module
# fib.py
def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)



# Using the module
from fib import fibonacci

res = fibonacci(8)
print("The result of fibonacci = ", res)