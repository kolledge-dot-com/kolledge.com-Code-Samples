# Control flow of while..else statement
index = 2
while index < 5:
    sqr = index ** 2
    print(f"Value of index = {index}")
    print(f"Square of index = {sqr}")
    print()
    index += 1
else:
    print("This is the Else block")
    print("For loop completed normally")
    print(f"Value of index = {index}")



# When execution of while loop does not complete normally
index = 2
while index < 5:
    sqr = index ** 2
    print(f"Value of index = {index}")
    print(f"Square of index = {sqr}")
    print()
    index += 1
    print("Executing break statement")
    break
else:
    print("This is the Else block")
    print("For loop completed normally")
    print(f"Value of index = {index}")
