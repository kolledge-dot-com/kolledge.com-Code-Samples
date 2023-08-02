# Match zero or more times (*) :
import re

pattern = r"ab*c"
string = "ac abc abbc abbbc abbbbc"
result = re.findall(pattern, string)
print(result)



# How Python Regex Greedy Mode Works :
import re

text = "the quick brown fox jumps over the lazy dog"
pattern = r"the.*?dog"
match = re.findall(pattern, text)
print(match)