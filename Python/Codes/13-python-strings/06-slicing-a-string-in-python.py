# Basic string slicing:
my_string = "Hello, Kolledge Scholars"
print(my_string[0])
print(my_string[7:15])




# Negative index slicing:
my_string = "Hello, Kolledge Scholars"
print(my_string[-1])
print(my_string[-8:-1])




# Step slicing:
my_string = "12345678"
print(my_string[::2])
print(my_string[::-1])
print(my_string[-1:-5:-1])




# Slicing and copying a string:
my_string = "Hello, Kolledge Scholars"
new_string = my_string[7:15]
print(new_string)




# Slicing with string methods:
my_string = "Hello, Kolledge Scholars"
start_index = my_string.find("Kolledge")
end_index = start_index + len("Kolledge")
sliced_string = my_string[start_index:end_index]
print(sliced_string)




# Using split() method to slice a string into a list of sub-strings:
my_string = "Hello, Kolledge, Scholars"
split_string = my_string.split(", ")
print(split_string)
print(split_string[1])