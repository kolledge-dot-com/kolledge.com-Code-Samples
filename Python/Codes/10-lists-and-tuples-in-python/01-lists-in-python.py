# Accessing elements of List
my_list = [1,2,3,4]
print(f"The first element of my_list = {my_list[0]}")
print(f"The second element of my_list = {my_list[1]}")
print(f"The last element of my_list = {my_list[-1]}")
print(f"The second last element of my_list = {my_list[-2]}")



# Change elements of a list
my_list = [1,2,3,4]
print("mylist = ", my_list)

# Changing element
my_list[2] = 100
print("mylist = ", my_list)



# Adding new element to the list
my_list = [1,2,3,4]
print("mylist = ", my_list)

# Adding element
my_list.append(100)
print("mylist = ", my_list)

# Inserting element
my_list.insert(2, 200)
print("mylist = ", my_list)




# Removing element using del keyword
my_list = [1,2,3,4]
print("mylist = ", my_list)

# using del keyword
del my_list[2]
print("mylist = ", my_list)



# Removing element using pop() method
my_list = [1,2,3,4]
print("mylist = ", my_list)
print()

# using pop method
e = my_list.pop()
print("mylist = ", my_list)
print("Popped element : ", e)
print()

# using pop method with index
e = my_list.pop(1)
print("mylist = ", my_list)
print("Popped element : ", e)



# Removing element using remove() method
my_list = [1,2,3,4]
print("mylist = ", my_list)
print()

# using remove method
my_list.remove(3)
print("mylist = ", my_list)