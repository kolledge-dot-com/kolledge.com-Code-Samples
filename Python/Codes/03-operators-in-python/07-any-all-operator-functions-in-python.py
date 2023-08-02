# Using any() and all() built-in functions
print(any([True, False, False]))
print(any([False, False, False]))
print(any(["a", "", "b"]))
print(any(["", "", ""]))


print(all([True, True, True]))
print(all([True, False, True]))
print(all(["a", "b", "c"]))
print(all(["a", "", "b"]))