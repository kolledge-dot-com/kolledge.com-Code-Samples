# convert string to datetime object
from datetime import datetime

dt_str = datetime.strptime('2018-06-01', '%Y-%m-%d')
print(dt_str)

dt_str = datetime.strptime('Jun 1 2018 1:33PM', '%b %d %Y %I:%M%p')
print(dt_str)




# How strptime() Works:
import datetime

# Parse the input string according to the format string
input_str = "2021-09-22 10:30:00"
dt = datetime.datetime.strptime(input_str, "%Y-%m-%d %H:%M:%S")

# Print the datetime object
print("Datetime object : ", dt)
print("Data Type of dt : ", type(dt))




# ValueError in strptime:
import datetime

# This will raise a ValueError
input_str = "2021/09/22"
dt = datetime.datetime.strptime(input_str, "%Y-%m-%d")