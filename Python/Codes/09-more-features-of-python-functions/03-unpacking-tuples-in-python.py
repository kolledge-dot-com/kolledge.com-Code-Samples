# Unpacking Tuples
tup = (10, 20, 30, 40)
var_1, var_2, var_3 = tup
print(var_1, var_2, var_3)


# Alternate syntax of unpacking tuples
var = 10, 20, 30
print(type(var))
var_1, var_2 = 10, 20
print(var_1, var_2)

# Unpacking - packing
tup = (10, 20, 30, 40, 50, 60)
var_1, var_2, *var_3 = tup
print(var_1)
print(var_2)
print(var_3)


# Merging Tuples
tup_1 = (10, 20, 30)
tup_2 = (40, 50, 60)
new_tuple = (*tup_1, *tup_2)
print(new_tuple)