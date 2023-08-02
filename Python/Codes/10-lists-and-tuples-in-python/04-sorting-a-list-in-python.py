# Sorting a list using sort() method
my_list = [3, 4, 1, 2]
print("my_list = ", my_list)


# Sorting the list
my_list.sort()
print("my_list = ", my_list)


# Sorting the list in reverse order
my_list.sort(reverse=True)
print("my_list = ", my_list)


my_str_list = ["lmno", "abc", "fgh", "xyz"]

# Sorting the list
my_str_list.sort()
print("my_str_list = ", my_str_list)


# Sorting the list in reverse order
my_str_list.sort(reverse=True)
print("my_str_list = ", my_str_list)



# Sorting list of Tuples
tup = [('John', 100), ('alice', 15), ('Steve', 200), ('Dave', 5)]
print("Tuple before sorting : ",tup)

tup.sort(key=lambda x: x[1])
print("Tuple after sorting : ", tup)



# Sorting List in Python using sorted function
my_list = [3, 4, 1, 2]
print("my_list = ", my_list)


# Sorting the list
new_list = sorted(my_list)
print("my_list = ", my_list)
print("new_list = ", new_list)


# Sorting the list in reverse order
new_list = sorted(my_list, reverse=True)
print("my_list = ", my_list)
print("new_list = ", new_list)


my_str_list = ["lmno", "abc", "fgh", "xyz"]

# Sorting the list
new_str_list = sorted(my_str_list)
print("my_str_list = ", my_str_list)
print("new_str_list = ", new_str_list)


# Sorting the list in reverse order
new_str_list = sorted(my_str_list, reverse=True)
print("my_str_list = ", my_str_list)
print("new_str_list = ", new_str_list)