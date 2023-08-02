# convert datetime to string using strftime()
import datetime

dt = datetime.datetime(2018, 1, 1)

d1 = dt.strftime('%A, %B %d')
print(d1)

d1 = dt.strftime('%c')
print(d1)

d1 = dt.strftime('%x')
print(d1)

d1 = dt.strftime('%X')
print(d1)





# How strftime() works
import datetime

# Create a datetime object
dt = datetime.datetime(2019, 9, 12, 10, 30, 0)

# Format the datetime object
formatted_str = dt.strftime("%Y-%m-%d %H:%M:%S")

# Print the formatted string
print(formatted_str)





# How to create string from a Timestamp
from datetime import datetime

timestamp = 1646153014.449067
dt_object = datetime.fromtimestamp(timestamp)

datetime_string = dt_object.strftime("%d-%b-%Y %H:%M:%S")
print("Datetime string:", datetime_string)




# Locale's Appropriate Date and Time
import datetime
import locale

# Set the locale
locale.setlocale(locale.LC_ALL, 'en_US')

# Create a datetime object
dt = datetime.datetime(2021, 9, 22, 10, 30, 0)

# Format the datetime object
formatted_str = dt.strftime("%c")

# Print the formatted string
print("Formatted String : ",formatted_str)
