# Creating dictionary using curly brackets
employees = {
    1: "John",
    2: "Peter",
    3: "John",
    4: "Alice"
}

print("employees is a dictionary.")
print(f"Data Type of employees is {type(employees)}")
print(f"Value of employees = ")
print(employees)


# Creating dictionary using dict class
employees = dict([(1, "John"), (2, "Peter"), (3, "John"),(4, "Alice")])

print("employees is a dictionary.")
print(f"Data Type of employees is {type(employees)}")
print(f"Value of employees = ")
print(employees)