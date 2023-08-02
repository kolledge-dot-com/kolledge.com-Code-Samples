import re

# Non-capturing group example
text = "The quick brown fox jumps over the lazy dog."
pattern = r"(?:quick|lazy)\s(\w+)"
result = re.findall(pattern, text)
print(result)