# Pass statement in Python
for index in range(2):
    print()
    print("This is the outer loop")
    print(f"Value of index = {index}")

    for cnt in range(3):
        pass


print()
print("Coming out of for loop")
print(f"Value of index = {index}")
