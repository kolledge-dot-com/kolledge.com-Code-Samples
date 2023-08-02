# Factorial Calculation through recursion
def factorial(n):
    if n == 0:
        print("Value of n = ", n)
        return 1
    else:
        print("Value of n = ", n)
        return n * factorial(n - 1)


fact = factorial(5)
print()
print("Final factorial value :", fact)


# Fibonacci Sequence through recursion
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

fibo = fibonacci(7)
print()
print("Final Fibonacci value :", fibo)