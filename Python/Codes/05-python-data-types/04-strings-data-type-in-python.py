# Accessing characters of a string
my_str = "abcdef"
print(my_str[0])
print(my_str[1])

# Accessing a Range of characters of string
my_str = "abcdef"
print(my_str[2:5])


my_str = "abcdef"
print(my_str[:5])
print(my_str[0:5])

my_str = "abcdef"
print(my_str[2:])
print(my_str[2:len(my_str)])


# Using negative indexes to access character of string
my_str = "abcdef"
print(my_str[-1])
print(my_str[-2])

my_str = "abcdef"
print(my_str[-3:-1])


# Strings are immutable
# Assigning a string to a variable
msg = "Kolledge Scholars!!"
print(msg)

# Output
# Kolledge Scholars!!



# Assigning new string literal to the same variable
msg = "hello Kolledge Scholars!!"
print(msg)

# Output
# hello Kolledge Scholars!!



# Accessing the characters of the string literal
c = msg[0]
print(c)

# Output
# h

# Trying to change the value of string literal
# This code gives error as strings are immutable
msg[0] = "H"
print(msg)

# Output
# TypeError: 'str' object does not support item assignment



# Common String Operations in Python

# Concatenating Strings in Python
string1 = "Hello!!!"
string2 = "Kolledge Scholars"
string3 = string1 + " " + string2
print(string3)

# Repeating a string in Python
string1 = "Hello_"
string2 = string1 * 3
print(string2)


# Check Sub-strings in Python
string1 = "Hello"
p = 'e' in string1
q = 'x' in string1
print (p)
print (q)


# Convert Strings to Uppercase or Lowercase
string1 = "Hello"
string2 = "WORLD"

string3 = string1.upper()
string4 = string2.lower()

print(string3)
print(string4)


# Strip a string in Python
string1 = " abcdef "
string2 = string1.strip()
print(string2)



