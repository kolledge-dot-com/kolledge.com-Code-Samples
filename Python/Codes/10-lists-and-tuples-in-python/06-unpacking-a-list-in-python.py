# Unpacking a list
my_list = [10, 20, 30]
print("my_list = ", my_list)

var_1, var_2, var_3 = my_list
print("var_1 = ", var_1)
print("var_2 = ", var_2)
print("var_3 = ", var_3)


# Unpacking - packing
my_list = [10, 20, 30, 40, 50, 60]
print("my_list = ", my_list)

var_1, var_2, *var_3 = my_list
print("var_1 = ", var_1)
print("var_2 = ", var_2)
print("var_3 = ", var_3)
