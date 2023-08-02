# get current date-time using datetime object
from datetime import datetime

now = datetime.now()
print("Current date and time:", now)



# get current UTC date-time using datetime object
from datetime import datetime

dt = datetime.now()

# Get the current date
current_utc_date = dt.utcnow()

print("Current UTC Date : ", current_utc_date)




# get current date-time in ISO format using datetime object

from datetime import datetime

now = datetime.now()
iso_time = now.isoformat()
print("Current date and time in ISO format:", iso_time)




# get date-time attributes using datetime object
from datetime import datetime

now = datetime.now()
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)
print("Microsecond:", now.microsecond)




# get current date using datetime object
from datetime import datetime

# Get datetime object
dt = datetime.now()

# Get the current date
current_date = dt.date()

print("Current Date : ", current_date)



# get timezone using datetime object

from datetime import datetime
import pytz

tz = pytz.timezone('US/Eastern')
now = datetime.now(tz)

print("Current date and time in US/Eastern:", now)
