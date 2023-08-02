# Using os.path.exists() function to check if a file exists
import os
file_path = "example.txt"
if os.path.exists(file_path):
   print(f"{file_path} exists.")
else:
   print(f"{file_path} does not exist.")




# Using the pathlib module to check if a file exists
from pathlib import Path
file_path = "example.txt"
if Path(file_path).exists():
   print(f"{file_path} exists.")
else:
   print(f"{file_path} does not exist.")