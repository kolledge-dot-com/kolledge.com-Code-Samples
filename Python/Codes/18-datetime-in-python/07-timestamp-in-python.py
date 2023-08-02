# Get Timestamp using time module in python :
import time

current_timestamp = time.time()
print("Current timestamp:", current_timestamp)





# Get Timestamp using calendar Module in python:
import calendar

time_tuple = (2022, 3, 7, 16, 0, 0)
timestamp = calendar.timegm(time_tuple)

print("Timestamp :", timestamp)



# Get Timestamp in Milliseconds:
import time

current_timestamp = time.time()
milliseconds_timestamp = int(current_timestamp * 1000)
print("Timestamp in milliseconds:", milliseconds_timestamp)



# Get the UTC Timestamp:
import time

current_utc_timestamp = time.mktime(time.gmtime())
print("Current UTC timestamp:", current_utc_timestamp)



# Get Timestamp from Datetime with a Different Timezone:
from datetime import datetime
import pytz

tz = pytz.timezone('US/Eastern')
now = datetime.now(tz)
timestamp = now.timestamp()

print("Timestamp with US/Eastern timezone:", timestamp)