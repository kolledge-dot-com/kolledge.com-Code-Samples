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