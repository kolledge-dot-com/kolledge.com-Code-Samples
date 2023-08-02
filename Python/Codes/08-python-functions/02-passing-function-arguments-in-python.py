# Parameters vs. Arguments

# Defining function calculate
def calculate(a, b):
    res = a + b
    return res


x = 2
y = 4
# calling the function calculate
s = calculate(x, y)

print("The sum of the two numbers is : ", s)


# Positional arguments in Python
def example(num, string):
    print(num)
    print(string)

example(10, "Hello")


# Keyword arguments in Python
def example(num, string):
    print(num)
    print(string)


example(string="Hello World", num=10)