# Using List comprehensions to filter elements in List

my_list = [10, 20, 30, 40]
print("my_list = ", my_list)

new_list = [x for x in my_list if 15 < x < 35]
print("new_list = ", new_list)