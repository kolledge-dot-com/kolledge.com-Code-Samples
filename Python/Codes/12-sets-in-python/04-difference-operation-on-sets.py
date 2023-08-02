# Difference operation using the difference method
set_1 = {1, 2, 3, 4}
set_2 = {2, 4, 5, 6, 7}
new_set = set_1.difference(set_2)
new_set_2 = set_2.difference(set_1)

print(f"Value of set_1 = {set_1}")
print(f"Value of set_2 = {set_2}")
print(f"Value of new_set = {new_set}")
print(f"Value of new_set_2 = {new_set_2}")



# Difference operation using the set difference operator '-'

set_1 = {1, 2, 3, 4}
set_2 = {2, 4, 5, 6, 7}
new_set = set_1 - set_2

print(f"Value of set_1 = {set_1}")
print(f"Value of set_2 = {set_2}")
print(f"Value of new_set = {new_set}")