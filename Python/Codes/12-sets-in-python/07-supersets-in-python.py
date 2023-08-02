# using issuperset() method
set_1 = {1, 2, 3}
set_2 = {1, 2, 3, 4, 5, 6, 7}
val = set_2.issuperset(set_1)

print(f"Value of set_1 = {set_1}")
print(f"Value of set_2 = {set_2}")
print(f"set_2 is superset of set_1 = {val}")



# using the superset operator '>='
set_1 = {1, 2, 3}
set_2 = {1, 2, 3, 4, 5, 6, 7}
val = set_2 >= set_1

print(f"Value of set_1 = {set_1}")
print(f"Value of set_2 = {set_2}")
print(f"set_2 is superset of set_1 = {val}")




# using the proper superset operator '>'
set_1 = {1, 2, 3}
set_2 = {1, 2, 3, 4, 5, 6, 7}
val = set_2 > set_1

print(f"Value of set_1 = {set_1}")
print(f"Value of set_2 = {set_2}")
print(f"set_2 is proper superset of set_1 = {val}")