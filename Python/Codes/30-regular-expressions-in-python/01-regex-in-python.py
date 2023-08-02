# search() Function
import re

string = "The quick brown fox jumps over the lazy dog."
pattern = "fox"

result = re.search(pattern, string)

if result:
    print("Pattern found!")
else:
    print("Pattern not found.")



# Match Object

import re

string = "The quick brown fox jumps over the lazy dog."
pattern = "brown"
result = re.search(pattern, string)

if result:
    match_start = result.start()
    match_end = result.end()
    print(f"Pattern found from index {match_start} to index {match_end}.")
else:
    print("Pattern not found.")


