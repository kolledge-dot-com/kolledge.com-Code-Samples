# The ^ Anchor :
import re

pattern = r"^Hello"
string = "Hello, world! How are you?"
result = re.findall(pattern, string)
print(result)