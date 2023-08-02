# Using Python loops
my_set = {1, 2, 3, 4}

sqr_set = set()
for i in my_set:
    sqr = i ** 2
    sqr_set.add(sqr)

print(f"Value of my_set = {my_set}")
print(f"Value of sqr_set = {sqr_set}")





# using map() function
my_set = {1, 2, 3, 4}

sqr_set_obj = map(lambda x: x ** 2, my_set)
sqr_set = set(sqr_set_obj)

print(f"Value of my_set = {my_set}")
print(f"Value of sqr_set = {sqr_set}")




# Set Comprehensions
my_set = {1, 2, 3, 4}
sqr_set = {x**2 for x in my_set}

print(f"Value of my_set = {my_set}")
print(f"Value of sqr_set = {sqr_set}")




# Using Set Comprehensions to transform elements

my_set = {1, 2, 3, 4}
sqr_set = {x**2 for x in my_set}

print(f"Value of my_set = {my_set}")
print(f"Value of sqr_set = {sqr_set}")



# Using Set Comprehensions to filter out elements
my_set = {10, 20, 30, 40, 50}
new_set = {x for x in my_set if x > 20}

print(f"Value of my_set = {my_set}")
print(f"Value of new_set = {new_set}")