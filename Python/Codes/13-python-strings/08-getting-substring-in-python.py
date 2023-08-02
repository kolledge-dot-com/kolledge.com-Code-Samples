# Basic sub-string slicing :
my_string = "Hello, Kolledge!"
substring = my_string[11:15]
print(substring)




# Negative index slicing:
my_string = "Hello, Kolledge!"
substring = my_string[-9:-1]
print(substring)




# Using String Methods:
my_string = "Hello, Kolledge!"
start_index = my_string.find("Kolledge")
length = len("Kolledge")
substring = my_string[start_index:start_index+length]
print(substring)




# Split the Original String:
my_string = "Hello, Kolledge!"
substrings = my_string.split(", ")
substring = substrings[1]
print(substring)




# Using Regular Expressions:
import re

my_string = "Hello 123 Kolledge Scholars."
pattern = r"\d+ \w+ \w+\."
match = re.search(pattern, my_string)
substring = match.group()
print(substring)



# Concatenating Sub-strings:
my_string = "Hello, Kolledge!"
substring1 = my_string[0:5]
substring2 = my_string[8:]
substring3 = "Python"
final_string = substring1 + " " + substring3
print(final_string)