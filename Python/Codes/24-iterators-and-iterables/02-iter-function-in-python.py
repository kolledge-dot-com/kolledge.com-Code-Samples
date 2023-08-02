# Code samples for Python iter() function :
my_list = [1, 2, 3, 4, 5]
my_iterator = iter(my_list)

# The next() method is used to get the next element from the iterator.
print(next(my_iterator))
print(next(my_iterator))



# second form of the Python iter() function :
def compare_values():
    x = 5
    while True:
        y = yield
        if y == x:
            return True


g = compare_values()
next(g)
result = iter(g.send, 5)



# Test if an object is iterable :
def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False


print(is_iterable('Hello'))
print(is_iterable([1, 2, 3]))
print(is_iterable({'a': 1, 'b': 2}))
print(is_iterable(20))
