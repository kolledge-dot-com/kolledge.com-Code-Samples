# time.sleep() function
import time

start_time = time.time()

for i in range(10):
    time.sleep(0.5)
    print(i, end=' ')

end_time = time.time()
print("Duration: {} seconds".format(end_time - start_time))
