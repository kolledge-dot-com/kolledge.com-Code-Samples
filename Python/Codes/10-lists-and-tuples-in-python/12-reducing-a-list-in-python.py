# Reducing list using loops
my_list = [10, 20, 30, 40, 50]
print("my_list = ", my_list)

sum = 0
for item in my_list:
    sum = sum + item

print("sum = ", sum)




# Reducing list using reduce() function
from functools import reduce


def logic_function(item_1, item_2):
    sum = item_1 + item_2
    return sum


my_list = [10, 20, 30, 40, 50]
print("my_list = ", my_list)

sum = reduce(logic_function, my_list)
print("sum = ", sum)




# Control flow of reduce function
from functools import reduce

my_list = [10, 20, 30, 40, 50]
print("my_list = ", my_list)

sum = reduce(lambda x, y: x + y, my_list)
print("sum = ", sum)