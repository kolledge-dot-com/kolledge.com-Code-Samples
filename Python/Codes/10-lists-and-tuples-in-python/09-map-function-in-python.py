# Transforming list elements Using loops
my_list = [1, 2, 3, 4]
print("my_list = ", my_list)

new_list = []
for item in my_list:
    sqr_item = item ** 2
    new_list.append(sqr_item)

print("new_list = ", new_list)



# Transforming list elements Using map() function
def trans_function(item):
    sqr_item = item ** 2
    return sqr_item


my_list = [1, 2, 3, 4]
print("my_list = ", my_list)

new_list_iterator = map(trans_function, my_list)
new_list = list(new_list_iterator)

print("new_list = ", new_list)




# Using Lambda expression within the map() function
my_list = [1, 2, 3, 4]
print("my_list = ", my_list)

new_list_iterator = map(lambda x: x ** 2, my_list)
new_list = list(new_list_iterator)

print("new_list = ", new_list)



# List comprehensions
my_list = [1, 2, 3, 4]
print("my_list = ", my_list)

new_list = [x ** 2 for x in my_list]
print("new_list = ", new_list)
