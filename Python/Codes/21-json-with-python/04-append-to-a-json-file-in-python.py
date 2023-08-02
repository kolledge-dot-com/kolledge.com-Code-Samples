# Appending to an Existing JSON File
import json

with open("example.json", "r") as f:
   data = json.load(f)
data["grades"] = [90, 85, 95]

with open("example.json", "w") as f:
   json.dump(data, f, indent=4)





# Appending data to Json using append method :
import json

with open('input.json', 'r') as file:
   data = json.load(file)

data.append({"name": "Mike"})

with open('input.json', 'w') as file:
   json.dump(data, file)