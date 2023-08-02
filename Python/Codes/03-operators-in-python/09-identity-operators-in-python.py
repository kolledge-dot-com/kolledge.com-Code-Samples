# is operator in Python

# The value and memory location of x and y are same
x = 10
y = x
res = x is y
print(res)


# The value of x and y is same
# But memory location is different
x = 10
y = float(x)
res = x is y
print(res)


# The '==' operator compares only value
x = 10
y = float(x)
res = x == y
print(res)


# is not operator in Python
x = 10
y = x
res = x is not y
print(res)
