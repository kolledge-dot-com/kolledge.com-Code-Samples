# Filtering elements using loops
my_list = [10, 20, 30, 40]
print("my_list = ", my_list)

new_list = []
for item in my_list:
    if 15 < item < 35:
        new_list.append(item)

print("new_list = ", new_list)



# Filtering elements using filter() function
def filter_function(item):
    if 15 < item < 35:
        return item


my_list = [10, 20, 30, 40]
print("my_list = ", my_list)

new_list_iterator = filter(filter_function, my_list)
new_list = list(new_list_iterator)

print("new_list = ", new_list)


# Filtering elements using lambda expressions with filter() function
my_list = [10, 20, 30, 40]
print("my_list = ", my_list)

new_list_iterator = filter(lambda x: 15 < x < 35, my_list)
new_list = list(new_list_iterator)

print("new_list = ", new_list)



# Filtering elements using List comprehensions
my_list = [10, 20, 30, 40]
print("my_list = ", my_list)

new_list = [x for x in my_list if 15 < x < 35]
print("new_list = ", new_list)