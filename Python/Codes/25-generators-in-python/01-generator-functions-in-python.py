# Python generator example :
def countdown(n):
   while n > 0:
       yield n
       n -= 1
for i in countdown(5):
   print(i)



# Creating iterators using generators :
def squares(n):
   for i in range(n):
       yield i

for i in squares(5):
   print(i)

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = (x for x in data if x % 2 == 0)
for i in evens:
   print(i)