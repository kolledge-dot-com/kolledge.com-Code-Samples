# get current time using now() function
from datetime import datetime

now = datetime.now()
current_time = now.time()
print("Current time:", current_time)




# get current time in UTC using datetime object
from datetime import datetime
import pytz

utc_now = datetime.now(pytz.utc)
utc_time = utc_now.strftime('%H:%M:%S %Z')
print("UTC time :", utc_time)



# Get current time using time module

# get the current time using time() function
import time

current_time = time.time()
print("Current time using time() function :", current_time)




# get the current time as a string
import time

current_time = time.ctime()
print("Current time :", current_time)


# get current time in milliseconds using time:
import time

current_time = round(time.time() * 1000)
print("Current time in milliseconds:", current_time)



# get current timein nanoseconds using time:
import time

current_time = time.perf_counter_ns()
print("Current time in nanoseconds:", current_time)



# get the current time using  localtime() function :
import time
from time import mktime
from datetime import datetime

local_time = time.localtime()
epoch_time = mktime(local_time)
curr_datetime = datetime.fromtimestamp(epoch_time)
curr_time = curr_datetime.time()

print("Current time :", curr_time)



# get current GMT time using time:
import time
from time import mktime
from datetime import datetime

current_gmt = time.gmtime()
epoch_time = mktime(current_gmt)
curr_datetime = datetime.fromtimestamp(epoch_time)
curr_time = curr_datetime.time()

print("Current GMT time:", curr_time)



# get current Time In Epoch using Time:
import time

current_time = int(time.time())
print("Current time in epoch format:", current_time)
