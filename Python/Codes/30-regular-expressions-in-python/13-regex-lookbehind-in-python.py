
import re

# Lookbehind example
text = "The quick brown fox jumps over the lazy dog."
pattern = r"(?<=quick\s)\b\w+\b"
result = re.findall(pattern, text)
print(result)