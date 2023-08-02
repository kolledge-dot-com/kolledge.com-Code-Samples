import re

# Alternation example
text = "The quick brown fox jumps over the lazy dog."
pattern = r"quick|lazy"
result = re.findall(pattern, text)
print(result)