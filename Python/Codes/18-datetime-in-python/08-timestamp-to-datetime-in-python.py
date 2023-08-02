# Converting timestamp to datetime object
from datetime import datetime

timestamp = 1646153014.449067
dt_object = datetime.fromtimestamp(timestamp)

print("Datetime Object :", dt_object)
print("Data type of dt_object :", type(dt_object))




# Converting timestamp to datetime string in specific format
from datetime import datetime

timestamp = 1646153014.449067
dt_object = datetime.fromtimestamp(timestamp)
datetime_string = dt_object.strftime("%d-%b-%Y %H:%M:%S")

print("Datetime string :", datetime_string)
print("Data type of dt_object datetime_string :", type(datetime_string))




# Converting timestamp to datetime string using str() function
from datetime import datetime

timestamp = 1646153014.449067
dt_object = datetime.fromtimestamp(timestamp)
dt_str = str(dt_object)

print("Datetime String :", dt_str)
print("Data type of dt_str :", type(dt_str))



# Converting timestamp to a datetime object in UTC

from datetime import datetime

# timestamp
ts = 1337961600

dt_utc = datetime.utcfromtimestamp(ts)

print(dt_utc)



# Converting datetime to timestamp

from datetime import datetime

now = datetime.now()
timestamp = datetime.timestamp(now)

print("Timestamp :", timestamp)