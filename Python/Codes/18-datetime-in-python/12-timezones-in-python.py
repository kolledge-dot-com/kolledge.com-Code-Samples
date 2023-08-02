# Creating a timezone aware datetime object using the timezone() method
import datetime
import pytz

local_zone = pytz.timezone('Europe/Warsaw')
local_time = datetime.datetime.now(local_zone)

print(local_time)




# Creating a timezone aware datetime object using the replace method
import datetime
import pytz

utc_now = datetime.datetime.now()
local_zone = pytz.timezone('Europe/Warsaw')
local_time = utc_now.replace(tzinfo=local_zone)

print("UTC Now : ", utc_now)
print("Local Time : ", local_time)



# Creating a timezone aware datetime object using the astimezone method
import datetime
import pytz

utc_time = datetime.datetime.utcnow()
utc_zone = pytz.utc
local_zone = pytz.timezone('Asia/Kolkata')
local_time = utc_time.astimezone(local_zone)

print("UTC Time : ", utc_time)
print("Local Time : ", local_time.strftime('%Y-%m-%d %H:%M:%S %Z%z'))



# Get current time in different timezone
import datetime
import pytz

local_zone = pytz.timezone('Asia/Kolkata')
local_time = datetime.datetime.now(local_zone)
utc_zone = pytz.utc
utc_time = local_time.astimezone(utc_zone)

print(f"Current Time in Asia/Kolkata: {local_time}")
print(f"Current Time in UTC: {utc_time}")



# get timezone information using tzinfo
import datetime
import pytz

local_zone = pytz.timezone('Asia/Kolkata')
local_time = datetime.datetime.now(local_zone)
tzinfo = local_time.tzinfo

print(tzinfo)



# convert between timezones
import datetime
import pytz

local_zone_1 = pytz.timezone('Europe/Warsaw')
local_zone_2 = pytz.timezone('America/New_York')
local_time_1 = datetime.datetime.now(local_zone_1)
local_time_2 = local_time_1.astimezone(local_zone_2)

print(f"Time in Asia/Kolkata: {local_time_1}")
print(f"Time in America/New_York: {local_time_2}")