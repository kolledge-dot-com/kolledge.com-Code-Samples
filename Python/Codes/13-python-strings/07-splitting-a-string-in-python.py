# Splitting a string using Iteration:
my_string = "Kolledge, Scholars"
delimiter = ", "
substrings = []
current_substring = ""
for character in my_string:
    if character == delimiter:
        substrings.append(current_substring)
        current_substring = ""
    else:
        current_substring += character
substrings.append(current_substring)
print(substrings)



# Splitting a string using regular expressions :
import re

my_string = "Kolledge, Scholars"
delimiter = ", "
substrings = re.split(delimiter, my_string)
print(substrings)





# Splitting a string using split method :
my_string = "Kolledge, Scholars"
delimiter = ", "
substrings = my_string.split(delimiter)
print(substrings)



# Splitting a string Using Itertools:
import itertools
my_string = "Kolledge, Scholars"
delimiter = ", "
substrings = [''.join(group) for is_delimiter, group in itertools.groupby(my_string, key=lambda x: x != delimiter) if is_delimiter]
print(substrings)



# Splitting a string Into a List of Characters:
my_string = "Kolledge, Scholars"
character_list = list(my_string)
print(character_list)



# Removing White-space with split():
my_string = "   Kolledge,     Scholars    "
substrings = my_string.split()
print(substrings)