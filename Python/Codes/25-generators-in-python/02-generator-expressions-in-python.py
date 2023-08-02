# Iterable vs iterator :
g = (x * 2 for x in range(3))
# Using the for loop
for i in g:
   print(i)
# Using the next() method
g = (x * 2 for x in range(3))
print(next(g))
print(next(g))
print(next(g))