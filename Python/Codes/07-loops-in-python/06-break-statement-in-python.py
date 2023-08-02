# break statement with for loop
for index in range(5):
    sqr = index ** 2
    print(f"Value of index = {index}")
    print(f"Square of index = {sqr}")
    print()

    if index % 3 == 1:
        print()
        print("break condition True.")
        break

print()
print("Coming out of for loop prematurely")
print(f"Value of index = {index}")


# Using break statement with while loop
index = 0
while index < 5:
    sqr = index ** 2
    print(f"Value of index = {index}")
    print(f"Square of index = {sqr}")
    print()

    if index % 3 == 1:
        print()
        print("break condition True.")
        break

    index += 1

print()
print("Coming out of while loop prematurely")
print(f"Value of index = {index}")



# Using break statement with nested loops
for index in range(2):
    print("-------------------------------------")
    print("Outer Loop")
    print(f"Value of index = {index}")

    print("Inner Loop")
    for cnt in range(4):
        print(f"Value of cnt = {cnt}")
        if cnt % 3 == 1:
            print("break condition True.")
            break

print()
print("Outer for loop completes normally.")
print(f"Value of index = {index}")