# Code sample of Using Yield in Python:
def countdown(num):
   while num > 0:
       yield num
       num -= 1
for i in countdown(5):
   print(i)




# Using Yield to Call Functions :

def countdown(num):
   while num > 0:
       yield num
       num -= 1
c = countdown(5)

print(next(c))
print(next(c))
print(next(c))