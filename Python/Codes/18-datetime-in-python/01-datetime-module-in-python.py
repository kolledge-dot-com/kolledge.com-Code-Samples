import datetime

# Get the current date and time
now = datetime.datetime.now()

# Print the current date and time
print(now)

# Print the current year, month, day, hour, minute, second, and microsecond
print(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)






# importing the module
import datetime

# Accessing datetime class
dt = datetime.datetime

print(dt.now())






# importing the class
from datetime import datetime

# Using datetime class
dt = datetime.now()

print(dt)





# Getting Current Date and Time
from datetime import datetime

# Get the current date and time
now = datetime.now()
print(now)
print()

# Print the current year, month, day, hour, minute, second, and microsecond
print(f"Current Year : {now.year}, \n"
      f"Current Month : {now.month}, \n"
      f"Current Day : {now.day}, \n"
      f"Current Hour : {now.hour}, \n"
      f"Current Minute : {now.minute},\n"
      f"Current Second : {now.second}, \n"
      f"Current microsecond : {now.microsecond}")




# Creating a Datetime Object
import datetime

dt = datetime.datetime(2009, 4, 12, 10, 20, 0, 44)

# Printing the datetime object
print("datetime object = ", dt)
print()


# Print the year, month, day, hour, minute, second, and microsecond of the date
print(f"Year : {dt.year}, \n"
      f"Month : {dt.month}, \n"
      f"Day : {dt.day}, \n"
      f"Hour : {dt.hour}, \n"
      f"Minute : {dt.minute},\n"
      f"Second : {dt.second}, \n"
      f"microsecond : {dt.microsecond}")




# Formatting a Datetime Object :
import datetime

# Creating a datetime object
dt = datetime.datetime(2015, 10, 25, 10, 30, 0)

# Formatting the datetime object
formatted_date = dt.strftime("%A, %d %B %Y %I:%M:%S %p")

print(formatted_date)




# Converting a String to a Datetime Object :
from datetime import datetime

# Convert a string to a datetime object
dt_string = "2015-10-25 10:30:00"
dt_object = datetime.strptime(dt_string, "%Y-%m-%d %H:%M:%S")

# Print the datetime object
print(dt_object)
