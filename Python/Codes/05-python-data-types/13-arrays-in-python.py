# creating array in Python
from array import *

my_list = [1, 2, 3, 4]

my_array = array('i',my_list)
my_array2 = array('i',[5, 6, 7, 8])

print(my_array)
print(my_array2)


# Accessing elements of array
my_list = [1, 2, 3, 4]
my_array = array('i',my_list)
print(my_array[0])     # prints 1
print(my_array[1])     # prints 2
print(my_array[2])     # prints 3


my_list = [1, 2, 3, 4]
my_array = array('i', my_list)
print(my_array[-1])     # prints 4
print(my_array[-2])     # prints 3



# Change the value of an element
my_list = [1, 2, 3, 4]
my_array = array('i', my_list)
my_array[0] = 10
print(my_array)


# Add elements to array
my_list = [1, 2, 3, 4]
my_array = array('i', my_list)
my_array.append(5)
print(my_array)


# Remove an element from array
my_list = [1, 2, 3, 4]
my_array = array('i', my_list)
my_array.remove(3)
print(my_array)


my_list = [1, 2, 3, 4]
my_array = array('i', my_list)
my_element = my_array.pop(0)
print(my_element)
print(my_array)


# Find the length of array
my_list = [1, 2, 3, 4]
my_array = array('i', my_list)
l = len(my_array)
print(l)


