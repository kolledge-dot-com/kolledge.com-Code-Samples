# Defining a set using curly braces
my_set = {1, 2, 3, 4}
print(f"Value of my_set = {my_set}")
print(f"Data Type my_set = {type(my_set)}")




# Defining a set using set() function
my_set = set([1, 2, 3, 4])
print(f"Value of my_set = {my_set}")

# Passing a tuple
my_set = set((10, 20, 30, 40))
print(f"Value of my_set = {my_set}")

# Passing duplicates
my_set = set([1, 2, 3, 4, 2, 3])
print(f"Value of my_set = {my_set}")



# Getting the number of elements of a set
my_set = {10, 20, 30, 40}
print(f"Value of my_set = {my_set}")
print(f"Length of my_set = {len(my_set)}")



# Fetching individual elements of a set
my_set = {1, 2, 3, 4}
print(f"Value of my_set = {my_set}")

print(f"Element at index 0 = {list(my_set)[0]}")
print(f"Element at index 1 = {list(my_set)[1]}")
print(f"Element at index 2 = {list(my_set)[2]}")

# Getting Last element of the set
print(f"Last Element of the set = {list(my_set)[-1]}")

print(f"First element of the set = {next(iter(my_set))}")


# Adding a new element to the set
my_set = {10, 20, 30, 40}
print(f"Value of my_set = {my_set}")

my_set.add(50)
print(f"Value of my_set = {my_set}")




# Removing an element from the set
my_set = {10, 20, 30, 40}
print(f"Value of my_set = {my_set}")

my_set.discard(30)
print(f"Value of my_set = {my_set}")

# Deleting element that is not present
my_set.discard(100)
print(f"Value of my_set = {my_set}")




# Removing all elements of the set
my_set = {10, 20, 30, 40}
print(f"Value of my_set = {my_set}")

# Deleting all elements of set
my_set.clear()
print(f"Value of my_set = {my_set}")

my_set = {1, 2, 3, 4}
print(f"Value of my_set = {my_set}")



# Checking if an element is present in the set
k = 3
if k in my_set:
    print(f"Element {k} is present in my_set")
else:
    print(f"Element {k} is not present in my_set")




# Returning an element from a set
my_set = {1, 2, 3, 4}
print(f"Value of my_set = {my_set}")

k = my_set.pop()
print(f"Element {k} was popped from my_set")

print(f"Value of my_set = {my_set}")






# Looping through all elements of set
my_set = {1, 2, 3, 4}
print(f"Value of my_set = {my_set}")
print()

print("Iterating through set elements")
for i in my_set:
    print(f"Value of element = {i}")
print()

print("Getting index of elements")
for index, item in enumerate(my_set):
    print(f"Element at index {index} = {item}")





# Frozen Sets
my_set = {1, 2, 3, 4}
print(f"Value of my_set = {my_set}")
print(f"Data Type of my_set = {type(my_set)}")
print()

my_frozen_set = frozenset(my_set)
print(f"Value of my_frozen_set = {my_frozen_set}")
print(f"Data Type of my_frozen_set = {type(my_frozen_set)}")
