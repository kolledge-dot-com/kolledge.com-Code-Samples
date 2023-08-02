# Iterators in Python
iterator = iter([1, 2, 3])

print(next(iterator))   # Output: 1
print(next(iterator))   # Output: 2
print(next(iterator))   # Output: 3
print(next(iterator))   # Output: StopIteration




# Iterables in Python :
iterable = [1, 2, 3]
iterator = iter(iterable)

print(next(iterator))   # Output: 1
print(next(iterator))   # Output: 2
print(next(iterator))   # Output: 3
print(next(iterator))   # Output: StopIteration



# Iterator vs Iterable
mylist = [1, 2, 3]
myiter = iter(mylist)

print(next(myiter))
print(next(myiter))
print(next(myiter))




#creating an iterator from a list
mylist = [1, 2, 3]
myiter = iter(mylist)

# traversing through the iterator
for x in myiter: print(x)



#creating an iterator from a tuple
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

# traversing through the iterator
for x in myit:
    print(x)




#creating an iterator from a string
mystr = "banana"
myit = iter(mystr)

# traversing through the iterator
for x in myit:
    print(x)




my_list = [1, 2, 3]
print(iter(my_list))




# python Iterator and Iterable :
class MyRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


my_range = MyRange(1, 4)
for value in my_range:
    print(value)




# Split an Iterator from an Iterable :
iterable = [1, 2, 3]
iterator = iter(iterable)

try:
   while True:
       value = next(iterator)
       print(value)
except StopIteration:
   pass