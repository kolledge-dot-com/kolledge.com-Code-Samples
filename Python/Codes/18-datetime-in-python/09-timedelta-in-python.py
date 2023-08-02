




# Creating a timedelta object
from datetime import timedelta

delta = timedelta(days=10, hours=5, minutes=30, seconds=20)
print("Timedelta:", delta)




# Creating a timedelta Object with weeks constructor
from datetime import timedelta

delta = timedelta(weeks=3)
print("Timedelta:", delta)




# Creating a timedelta object with days constructor
from datetime import timedelta

delta = timedelta(days=20)
print("Timedelta:", delta)





# Creating timedelta object with hours constructor:
from datetime import timedelta

delta = timedelta(hours=122)
print("Timedelta:", delta)




# Creating a timedelta object with seconds constructor:
from datetime import timedelta

delta = timedelta(seconds=3600)
print("Timedelta:", delta)





# Creating a timedelta object with microseconds constructor:
from datetime import timedelta

delta = timedelta(microseconds=500000)
print("Timedelta:", delta)





# Find the difference between two dates
from datetime import date

d1 = date(2017, 5, 19)
d2 = date(2017, 5, 15)

# Getting the difference between two dates
diff = d1 - d2
print("Time Diff :", diff)
print("Data type of diff : ", type(diff))
print()




# Add a time duration to a datetime object.
from datetime import datetime
from datetime import timedelta

# Adding a time duration to a datetime object
dt = datetime(2017, 5, 9)
new_date = dt + timedelta(days=7)

print("Orig. date :", dt)
print("New date   :", new_date)
print("Data type of New date :", type(new_date))
print()




# Subtract a time duration from a datetime object.
from datetime import datetime
from datetime import timedelta

# Subtracting a time duration to a datetime object
dt = datetime(2017, 5, 9)
new_date = dt - timedelta(days=7)

print("Orig. date :", dt)
print("New date   :", new_date)
print("Data type of New date :", type(new_date))
print()





# Add a time duration to a date object.
from datetime import date
from datetime import timedelta

# Adding a time duration to a date object
d = date(2017, 5, 19)
new_date = d + timedelta(days=7)

print("Orig. date :", d)
print("New date   :", new_date)
print("Data type of New date :", type(new_date))
print()





# Subtract a time duration from a date object.
from datetime import date
from datetime import timedelta

# Subtracting a time duration to a date object
d = date(2017, 5, 19)
new_date = d - timedelta(days=7)

print("Orig. date :", d)
print("New date   :", new_date)
print("Data type of New date :", type(new_date))
print()




# Add two timedelta objects
from datetime import timedelta

delta1 = timedelta(days=10)
delta2 = timedelta(hours=12)
result = delta1 + delta2

print("Result:", result)




# Subtract two timedelta objects
from datetime import timedelta

delta1 = timedelta(days=10)
delta2 = timedelta(days=4, hours=10)
result = delta1 - delta2

print("Result:", result)





# Compare two timedelta objects
from datetime import timedelta

delta1 = timedelta(days=10)
delta2 = timedelta(days=9, hours=10)

if delta1 > delta2:
   print("delta1 is greater than delta2")
else:
   print("delta1 is less than or equal to delta2")




# Timedelta Attributes:
from datetime import timedelta

delta = timedelta(days=10, hours=5, minutes=30, seconds=20, microseconds=30)

print("Days :", delta.days)
print("Seconds :", delta.seconds)
print("Microseconds :", delta.microseconds)




# Converting timedelta object to seconds
from datetime import timedelta

delta = timedelta(hours=1, minutes=30, seconds=20)

seconds = delta.total_seconds()
print("Total seconds:", seconds)




# Formatting a timedelta object
from datetime import timedelta

delta = timedelta(days=10, hours=5, minutes=30, seconds=20)

delta_string = str(delta)
print("Timedelta string:", delta_string)



# convert string to timedelta
import datetime

str_td = "15:12:40"
dt = datetime.datetime.strptime(str_td, "%H:%M:%S")

# Calculating total number of seconds
total_sec = dt.hour*3600 + dt.minute*60 + dt.second
td = datetime.timedelta(seconds=total_sec)

print("Timedelta : ",td)
print("Data Type of td : ", type(td))