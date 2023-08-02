# Getting the type of an Integer variable in Python
index = 100

print(type(index))




# Getting the size of an Integer in Python
from sys import getsizeof

num_1 = 0
num_2 = 200
num_3 = 2 ** 32

size_num_1 = getsizeof(num_1)
size_num_2 = getsizeof(num_2)
size_num_3 = getsizeof(num_3)

print("Size of num_1 : ", size_num_1)
print("Size of num_2 : ", size_num_2)
print("Size of num_3 : ", size_num_3)