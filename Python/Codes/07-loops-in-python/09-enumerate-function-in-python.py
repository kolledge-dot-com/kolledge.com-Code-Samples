# Enumerate function with a list
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit)


# Enumerate function with a string
message = "Hello"
for index, char in enumerate(message):
    print(index, char)


# Enumerate function with a tuple
animals = ('cat', 'dog', 'rabbit')
for index, animal in enumerate(animals):
    print(index, animal)


# Enumerate function with a dictionary
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
for index, key in enumerate(scores):
    print(index, key, scores[key])


# Specifying the start value for enumeration
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)


# Enumerate function with nested loops
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i, row in enumerate(matrix):
    for j, value in enumerate(row):
        print(i, j, value)


# Enumerate function with unpacking
coordinates = [(1, 2), (3, 4), (5, 6)]
for index, (x, y) in enumerate(coordinates):
    print(index, x, y)