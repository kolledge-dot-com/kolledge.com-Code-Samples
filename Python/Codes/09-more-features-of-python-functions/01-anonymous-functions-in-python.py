# Anonymous Functions in Python
f = lambda x, y: x + y
s = f(1, 2)
print(s)


# Passing Anonymous functions as arguments
def apply_func(x, func):
    return func(x)


s = apply_func(2, lambda x: x * x)
print(s)

# sort a list of data by some criteria
strings = ['foo', 'bar', 'ba', 'q', 'quux']
sorted_strings = sorted(strings, key=lambda s: len(s))
print(sorted_strings)


# create small throwaway functions on the fly
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x * x, numbers)
print(list(squared))