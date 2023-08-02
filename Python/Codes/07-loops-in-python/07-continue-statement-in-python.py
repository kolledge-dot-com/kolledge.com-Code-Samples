# Using continue statement with for loop
for index in range(5):
    if index % 2 == 1:
        print()
        print(f"skipping index value {index}")
        index += 1
        continue

    sqr = index ** 2
    print()
    print(f"Value of index = {index}")
    print(f"Square of index = {sqr}")

print()
print("Coming out of for loop")
print(f"Value of index = {index}")



# Using continue statement with while loop
index = 0
while index < 5:
    if index % 2 == 1:
        print()
        print(f"skipping index value {index}")
        index += 1
        continue

    sqr = index ** 2
    print()
    print(f"Value of index = {index}")
    print(f"Square of index = {sqr}")

    index += 1

print()
print("Coming out of while loop")
print(f"Value of index = {index}")



# Using continue statement with nested loops
for index in range(2):
    print("-------------------------------------")
    print("Outer Loop")
    print(f"Value of index = {index}")

    print("Inner Loop")
    for cnt in range(4):
        print(f"Value of cnt = {cnt}")
        if cnt % 3 == 1:
            print("continue condition True.")
            continue

print()
print("Coming out of outer for loop")
print(f"Value of index = {index}")
