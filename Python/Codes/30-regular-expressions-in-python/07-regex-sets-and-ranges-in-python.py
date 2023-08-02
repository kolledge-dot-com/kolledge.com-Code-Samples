# Sets in Regex :
import re

text = "abcdefg"
pattern = r"[a-c]"
result = re.findall(pattern, text)
print(result)  # Output: ['a', 'b', 'c']