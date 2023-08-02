# Regex Non-Greedy (or Lazy) Quantifiers :

import re
text = "fruit:apple, fruit:banana, fruit:cherry"
pattern = r"fruit:(.*?),"
result = re.findall(pattern, text)
print(result)