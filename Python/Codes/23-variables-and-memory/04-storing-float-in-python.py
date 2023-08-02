# Using float() function in Python
num_1 = float("2.5")
num_2 = float(20)

print(num_1)
print(type(num_1))

print(num_2)
print(type(num_2))




# Comparing floats
x = 1.2 + 1.2 + 1.2
y = 3.6

print(x == y)




x = 1.2 + 1.2 + 1.2
y = 3.6

print(x == y)
print(x)
print(y)



# Using format method
x = 1.2 + 1.2 + 1.2
y = 3.6

print(format(x, '.30f'))
print(format(y, '.30f'))



# Infinite digits
x = 1.2 + 1.2 + 1.2
y = 3.6

print(format(x, '.60f'))
print(format(y, '.60f'))



# Using isclose() function
from math import isclose

x = 1.2 + 1.2 + 1.2
y = 3.6

print(isclose(x,y))