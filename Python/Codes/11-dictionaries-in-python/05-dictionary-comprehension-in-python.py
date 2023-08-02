# Dictionary comprehension
quantities = {
    "apple": 10,
    "oranges": 20,
    "banana": 25,
    "Mangoes": 35
}

print("Getting fruits with quantity > 20")
fruits = {key:value for (key,value) in quantities.items() if value > 20}

print(f"Fruits with qnt > 20  = {fruits}")




# Transforming a dictionary using dictionary comprehension
quantities = {
    "apple": 10,
    "oranges": 20,
    "banana": 25,
    "Mangoes": 35
}

print(f"Quantities  = {quantities}")
print()

print("If quantity is more than 20 - set it to 15")
quantities.update({key:15 for key in quantities if quantities[key] > 20})
print(f"New Quantities  = {quantities}")



# Filtering dictionary elements using dictionary comprehension
quantities = {
    "apple": 0,
    "oranges": 20,
    "banana": 0,
    "Mangoes": 35
}

print("Getting Out of stock fruits")
fruits = {key:value for (key,value) in quantities.items() if value == 0}

print(f"Out of stock fruits  = {fruits}")