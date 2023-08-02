# do...while loop in Python
index = 2
while True:
    sqr = index ** 2
    print(f"Value of index = {index}")
    print(f"Square of index = {sqr}")
    print()
    index += 1

    if index == 5:
        break
