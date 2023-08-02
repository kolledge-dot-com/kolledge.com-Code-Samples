# Adding new key-value pairs to a dictionary
quantities = {
    "apple": 10,
    "oranges": 20,
    "banana": 25,
    "Mangoes": 35
}

print("Printing Quantities of fruits :")
print("Quantity of apples = ", quantities.get("apple"))
print("Quantity of oranges = ", quantities.get("oranges"))
print("Quantity of banana = ", quantities.get("banana"))
print("Quantity of Mangoes = ", quantities.get("Mangoes"))

# Adding new key-value pair
quantities["Guavas"] = 50
print("Quantity of Guavas = ", quantities.get("Guavas"))