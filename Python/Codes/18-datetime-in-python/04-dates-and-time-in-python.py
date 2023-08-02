# Today's Date in Python:
from datetime import date

today = date.today()
print("Today's date:", today)




# Current Date in Different Formats:
from datetime import datetime

# Formats: year, month, day
print(datetime.now().strftime("%Y-%m-%d"))
print(datetime.now().strftime("%d-%m-%Y"))
print(datetime.now().strftime("%A %d %B %Y"))




# Get the Current Date and Time in Python
from datetime import datetime

now = datetime.now()
print("Current date and time:", now)