# The \b Word Boundary :
import re
pattern = r"\bapple\b"
string = "I have an apple and a pineapple."
result = re.findall(pattern, string)
print(result)