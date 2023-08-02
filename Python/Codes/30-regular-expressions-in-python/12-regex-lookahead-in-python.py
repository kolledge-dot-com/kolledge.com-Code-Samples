import re

# Lookahead example
text = "The quick brown fox jumps over the lazy dog."
pattern = r"\w+(?=\sfox)"
result = re.findall(pattern, text)
print(result)