# Modifying the values of the key-value pairs
quantities = {
    "apple": 10,
    "oranges": 20,
    "banana": 25,
    "Mangoes": 35
}

print("Value os dictionary :")
print(quantities)
print()

quantities["apple"] = 5
print("Value os dictionary :")
print(quantities)



# Deleting a key-value pair
quantities = {
    "apple": 10,
    "oranges": 20,
    "banana": 25,
    "Mangoes": 35
}

print("Value os dictionary :")
print(quantities)
print()

del quantities["apple"]
print("Value os dictionary :")
print(quantities)