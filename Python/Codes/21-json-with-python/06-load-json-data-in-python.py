# Json.load() method :
import json

# Opening JSON file
f = open('test.json', )

# returns JSON object as
# a dictionary
jdata = json.load(f)

# Iterating through the json
# list
for i in jdata['test_details']:
    print(i)

# Close the file
f.close()





# json.loads() method :
import json

# JSON string:
# Multi-line string containing json data
jstring = """{
    "Emp-Id": "2398",
    "Emp-Name":"Tom Grooves",
    "Contact": 70079865453,
    "Email-Id": "tgrooves@gmail.com",
    }"""

# parse jstring :
d = json.loads(jstring)

# the result is a Python dictionary:
print(d)