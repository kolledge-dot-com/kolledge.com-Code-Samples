# Slicing a list in Python
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
print("my_list = ", my_list)


# Slicing Using values of begin end and steps
sub_list = my_list[2:6:2]
print("sub_list = ", sub_list)




# Slicing Using default values of end and steps
sub_list = my_list[2:]
print("my_list = ", my_list)
print("sub_list = ", sub_list)




# Slicing Using default values of begin and steps
sub_list = my_list[:4:]
print("my_list = ", my_list)
print("sub_list = ", sub_list)




# Slicing Using negative value of begin
sub_list = my_list[-3:]
print("my_list = ", my_list)
print("sub_list = ", sub_list)



# get the first n-elements of a list in Python
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
print("my_list = ", my_list)

n = 5
sub_list = my_list[:n]
print("sub_list = ", sub_list)



# get the last n-elements of a list in Python
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
print("my_list = ", my_list)

n = 5
sub_list = my_list[-n:]
print("sub_list = ", sub_list)



# get every nth element of the list in Python
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
print("my_list = ", my_list)

n = 3
sub_list = my_list[::n]
print("sub_list = ", sub_list)



# reverse a list in Python using slicing
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
print("my_list = ", my_list)

rev_list = my_list[::-1]
print("rev_list = ", rev_list)


# substitute a part of the list in Python
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
print("my_list = ", my_list)

my_list[2:5] = [300, 400, 500]
print("my_list = ", my_list)



# resize the list in Python
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
print("my_list = ", my_list)

my_list[2:5] = [300, 400, 500, 550, 560]
print("my_list = ", my_list)



# delete list element using slicing in Python
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
print("my_list = ", my_list)

del my_list[2:5]
print("my_list = ", my_list)