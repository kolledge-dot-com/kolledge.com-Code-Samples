# Encoding JSON Data in Python :
import json

person = {
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

json_data = json.dumps(person)
print(json_data)



# Decoding JSON Data in Python :
import json

json_data = '{"name": "John", "age": 30, "isStudent": true, "subjects": ["English", "Maths", "Science"], "address": {"street": "123 Main St", "city": "New York", "state": "NY", "zip": "10001"}}'

person = json.loads(json_data)
print(person)





# Reading JSON Data from a File :
import json

with open('person.json', 'r') as f:
    person = json.load(f)

print(person)





# Writing JSON Data to a File :
import json

person = {
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

with open('person.json', 'w') as f:
    json.dump(person, f)






# Handling Errors in JSON :
import json

json_data = 'invalid json data'

try:
   person = json.loads(json_data)
except json.JSONDecodeError as e:
   print(f"Error decoding JSON data: {e}")