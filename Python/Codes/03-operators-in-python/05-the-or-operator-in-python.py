# When at-least one conditions is True
# it returns True
x = True
y = True
res = x or y
print(res)


# When at-least one conditions is True
# it returns True
x = True
y = False
res = x or y
print(res)


# When both the conditions are False
# it returns False
x = False
y = False
res = x or y
print(res)


# If one or more operands is an arithmetic value,
# it returns the first value
x = True
y = 100
res = x or y
print(res)


# If one or more operands is an arithmetic value,
# it returns the first value
x = 100
y = True
res = x or y
print(res)
