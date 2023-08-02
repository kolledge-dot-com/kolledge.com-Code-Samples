# Looping through all elements of a dictionary
quantities = {
    "apple": 10,
    "oranges": 20,
    "banana": 25,
    "Mangoes": 35
}

print("Looping through items of dictionary ")
for key, value in quantities.items():
    print(f"Quantity of {key} = {value}",)




# Looping through all keys of a dictionary
quantities = {
    "apple": 10,
    "oranges": 20,
    "banana": 25,
    "Mangoes": 35
}

print("Looping through items of dictionary ")
for key in quantities.keys():
    print(f"Quantity of {key} = {quantities[key]}")

print()
available_fruits = list(quantities.keys())
print("List of available fruits : ", available_fruits)




# Looping through all values of a dictionary
quantities = {
    "apple": 10,
    "oranges": 20,
    "banana": 25,
    "Mangoes": 35
}

stock = 0
print("Calculating total stock")
for value in quantities.values():
    stock = stock + value

print(f"Total fruits available = {stock}")