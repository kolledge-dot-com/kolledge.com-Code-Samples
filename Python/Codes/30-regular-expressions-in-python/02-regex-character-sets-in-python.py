# \d: Digit Character Set
import re

pattern = r"\d"
string = "There are 123 apples"
result = re.findall(pattern, string)
print(result)