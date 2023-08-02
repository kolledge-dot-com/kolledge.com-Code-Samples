
# Creating Sets in Python

# Creating a set using curly braces {}
s1 = {1, 2, 3}

# Creating an empty set
s2 = set()

# Creating a set using the set() function
s3 = set([1, 2, 3])

# Creating a set from a list
s4 = set([1, 2, 3, 1, 2, 3])

# Creating a set from a tuple
s5 = set((1, 2, 3))

# Creating a set from a string
s6 = set("abc")

# Creating a set from a dictionary
s7 = set({"a": 1, "b": 2, "c": 3})

print("s1 = ", s1)
print("s2 = ", s2)
print("s3 = ", s3)
print("s4 = ", s4)
print("s5 = ", s5)
print("s6 = ", s6)
print("s7 = ", s7)


# access the values in a set
s1 = {1, 2, 3}
for value in s1:
    print(value)


# check if a value is in a set
s1 = {1, 2, 3}
if 1 in s1:
    print("1 is in s1")



# add values to a set
s1 = {1, 2, 3}
s1.add(4)


# remove values from a set
s1 = {1, 2, 3}
s1.remove(2)


# find the length of a set
s1 = {1, 2, 3}
print(len(s1))

# clear a set
s1 = {1, 2, 3}
s1.clear()


# Frozenset data type in Python
fs = frozenset([1, 2, 3])
print(fs)
print(f"Data Type of fs is {type(fs)}")