# Accessing values Using square bracket notation
quantities = {
    "apple": 10,
    "oranges": 20,
    "banana": 25,
    "Mangoes": 35
}

print("Printing Quantities of fruits :")
print("Quantity of apples = ", quantities["apple"])
print("Quantity of oranges = ", quantities["oranges"])
print("Quantity of banana = ", quantities["banana"])
print("Quantity of Mangoes = ", quantities["Mangoes"])




# Accessing values using the get() method
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

print("Quantity of Guavas = ", quantities.get("Guavas"))
print("Quantity of Guavas = ", quantities.get("Guavas", "Zero"))
