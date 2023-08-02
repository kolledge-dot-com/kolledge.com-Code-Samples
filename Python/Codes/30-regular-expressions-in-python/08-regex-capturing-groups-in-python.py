import re

# Capturing group example
text = "The quick brown fox jumps over the lazy dog."
pattern = r"The quick (.*?) fox"
result = re.findall(pattern, text)
print(result)