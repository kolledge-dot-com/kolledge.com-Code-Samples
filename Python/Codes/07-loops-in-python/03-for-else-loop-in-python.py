# Control flow of for..else statement
for index in range(2, 5):
    sqr = index ** 2
    print(f"Value of index = {index}")
    print(f"Square of index = {sqr}")
    print()
else:
    print("This is the Else block")
    print("For loop completed normally")



#  When execution of for loop does not complete normally
for index in range(2, 5):
    sqr = index ** 2
    print(f"Value of index = {index}")
    print(f"Square of index = {sqr}")
    print()
    print("Executing break statement")
    break
else:
    print("This is the Else block")
    print("For loop completed normally")
