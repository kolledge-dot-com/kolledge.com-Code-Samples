# Opening and Reading JSON Files in Python :
import json

with open("example.json", "r") as f:
    data = json.load(f)

print(data)




# Accessing Values from JSON Data :
import json

with open("example.json", "r") as f:
    data = json.load(f)

print(data["name"])
print(data["age"])
print(data["subjects"][0])




# Working with Nested JSON Data
import json

with open("example.json", "r") as f:
    data = json.load(f)

print(data["address"]["city"])
print(data["grades"][1]["marks"][2])




# Handling Errors when Reading JSON Files

import json

try:
   with open("example.json", "r") as f:
       data = json.load(f)
except json.JSONDecodeError as e:
   print(f"JSON decoding error: {e}")