# using issubset() method
set_1 = {1, 2, 3}
set_2 = {1, 2, 3, 4, 5, 6, 7}
val = set_1.issubset(set_2)

print(f"Value of set_1 = {set_1}")
print(f"Value of set_2 = {set_2}")
print(f"set_1 is subset of set_2 = {val}")



# using the subset operator '<='
set_1 = {1, 2, 3}
set_2 = {1, 2, 3, 4, 5, 6, 7}
val = set_1 <= set_2

print(f"Value of set_1 = {set_1}")
print(f"Value of set_2 = {set_2}")
print(f"set_1 is subset of set_2 = {val}")




# using the proper subset operator '<'
set_1 = {1, 2, 3}
set_2 = {1, 2, 3, 4, 5, 6, 7}
val = set_1 < set_2

print(f"Value of set_1 = {set_1}")
print(f"Value of set_2 = {set_2}")
print(f"set_1 is proper subset of set_2 = {val}")