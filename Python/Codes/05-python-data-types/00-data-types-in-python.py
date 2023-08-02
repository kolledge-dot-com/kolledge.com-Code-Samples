# Changing Data type through reassignment
var_x = 20
print("Type of var_x : ", type(var_x))

var_x = 20.5
print("Type of var_x : ", type(var_x))

var_y = 12.20
print("Type of var_y : ", type(var_y))

var_y = 50
print("Type of var_y : ", type(var_y))


# Changing Data type through type casting
var_x = 20
print("Type of var_x : ", type(var_x))

var_x = float(var_x)
print("Type of var_x : ", type(var_x))

var_y = 12.20
print("Type of var_y : ", type(var_y))

var_y = int(var_y)
print("Type of var_y : ", type(var_y))


# type() function
index = 20
print("Type of index : ", type(index))

# isinstance() function
index = 20
t = isinstance(index, int)
print(t)


# Mutable Data types in Python
my_list = [10, 20, 30]
print(my_list)

# Adding one more element to the list
my_list.append(40)
print(my_list)



# Immutable Data types in Python

# Assigning a string literal to a variable
message = "hello Kolledge Scholars!!"
print(message)

# Assigning another string literal to the same variable
message = "howdy Kolledge Scholars!!"
print(message)

# Accessing the first character of the string literal
ch = message[0]
print(ch)

# Trying to change the value of string literal
# gives error as strings are immutable
message[0] = "H"
print(message)