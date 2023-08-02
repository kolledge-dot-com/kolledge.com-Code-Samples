# write Pretty-printed JSON Data into a File
import json

data = {'name': 'John', 'age': 30, 'city': 'New York'}

# Writing pretty-printed JSON data to a file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)





# PrettyPrint JSON File in Python :
import json

# Reading and pretty-printing JSON data from a file
with open('data.json') as file:
   data = json.load(file)
   pretty_data = json.dumps(data, indent=4)
   print(pretty_data)




# Using pprint Module to Pretty-print JSON :
import json
import pprint

data = {'name': 'John', 'age': 30, 'city': 'New York'}

# Pretty-printing JSON data using pprint
pprint.pprint(data, indent=4)