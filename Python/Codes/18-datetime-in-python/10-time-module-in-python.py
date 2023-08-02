# get time string from seconds
import time

seconds_since_epoch = 1646882186.9547188
time_string = time.ctime(seconds_since_epoch)
print("Time String:", time_string)




# delay execution of programs in python
import time

print("Executing...")
time.sleep(3)
print("...Delayed Execution")




# represent time in a structured way
import time

current_time = time.localtime()

print("Current Time:", current_time)
print("Year:", current_time.tm_year)




# Frequently used functions of time Module

import time

current_time = time.time()
print("Current Time:", current_time)



current_time = time.time()
time_string = time.ctime(current_time)

print("Time String:", time_string)



print("Executing...")
time.sleep(3)
print("...Delayed Execution")



from time import process_time

n = 500000

# Start timing
start_time = process_time()

sum = 0
for i in range(n):
    sum = sum + n ^ 2

# Stop timing
stop_time = process_time()

print("Start time:", start_time)
print("Stop time:", stop_time)
print("Elapsed time during the whole program in seconds:", stop_time - start_time)




current_time = time.localtime()
print("Current Time:", current_time)




current_time = time.gmtime()
print("Current Time in UTC:", current_time)



current_time = time.localtime()
seconds_since_epoch = time.mktime(current_time)
print("Seconds since Epoch:", seconds_since_epoch)



current_time = time.localtime()
time_string = time.asctime(current_time)

print("Time String:", time_string)



current_time = time.localtime()
time_string = time.strftime("%Y-%m-%d %H:%M:%S", current_time)

print("Time String:", time_string)




time_string = "2020-03-22 07:22:07"
current_time = time.strptime(time_string, "%Y-%m-%d %H:%M:%S")

print("Current Time:", current_time)
