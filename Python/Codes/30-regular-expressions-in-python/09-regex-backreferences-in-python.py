
import re

# Backreference example
text = "The quick brown fox jumps over the lazy dog."
pattern = r"\b(\w+)\s+\1"
result = re.findall(pattern, text)
print(result)