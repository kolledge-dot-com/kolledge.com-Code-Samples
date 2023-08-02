# json.dump() Method :
import json

data = {'name': 'John Doe', 'age': 42, 'city': 'New York'}

with open('data.json', 'w') as f:
    json.dump(data, f)





# json.dumps() Method :
import json
data = {'name': 'John Doe', 'age': 42, 'city': 'New York'}

with open('data.json', 'w') as f:
   f.write(json.dumps(data))





# Creating and Writing JSON Data :
import json

data = {
   "name": "John",
   "age": 30,
   "isStudent": True,
   "subjects": ["English", "Maths", "Science"],
   "address": {
       "street": "123 Main St",
       "city": "New York",
       "state": "NY",
       "zip": "10001"
   }
}

json_data = json.dumps(data)
with open("example.json", "w") as f:
   f.write(json_data)




# Writing Pretty JSON Data :
import json

data = {
   "name": "John",
   "age": 30,
   "isStudent": True,
   "subjects": ["English", "Maths", "Science"],
   "address": {
       "street": "123 Main St",
       "city": "New York",
       "state": "NY",
       "zip": "10001"
   }
}

json_data = json.dumps(data, indent=4)
with open("example.json", "w") as f:
   f.write(json_data)




# Appending to an Existing JSON File
import json

with open("example.json", "r") as f:
   data = json.load(f)

data["grades"] = [90, 85, 95]
with open("example.json", "w") as f:
   json.dump(data, f, indent=4)




# Handling Errors when Writing JSON Files
import json

data = {
    "name": "John",
    "age": 30,
    "isStudent": True,
    "subjects": ["English", "Maths", "Science"],
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "state": "NY"
    }
}

try:
    json_data = json.dumps(data)
except json.JSONEncodeError as e:
    print(f"JSON encoding error: {e}")
else:
    with open("example.json", "w") as f:
        f.write(json_data)
