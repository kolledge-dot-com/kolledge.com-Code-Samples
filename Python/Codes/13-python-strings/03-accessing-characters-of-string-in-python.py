# Accessing a single character of a string:
my_str = "Hello, world!"
print(my_str[0])  # H
print(my_str[4])  # o
print(my_str[-1])  # !
print(my_str[-2])  # !




# Accessing a range of characters of a string:
my_string = "Hello, world!"
print(my_string[0:5])    # Hello
print(my_string[7:])     # world!
print(my_string[:5])     # Hello



# Accessing every nth character of a string:
my_string = "12345678"
print(my_string[::2])



# Modifying characters of a string:
my_string = "Hello, world!"
new_string = my_string[:6] + "Kolledge!"
print(new_string)