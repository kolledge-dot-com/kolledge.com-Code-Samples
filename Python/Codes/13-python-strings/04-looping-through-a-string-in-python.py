# Using a for loop:
my_string = "Hello"
for character in my_string:
    print(character)


# Using a while loop:
my_string = "Hello"
index = 0
while index < len(my_string):
    print(my_string[index])
    index += 1


# Using range() function:
my_string = "Hello"
for index in range(len(my_string)):
    print(my_string[index])




# Skipping characters:
my_string = "Hello"
for character in my_string:
    if character == 'l':
        continue
    print(character)




# Breaking out of the loop:
my_string = "Hello"
for character in my_string:
    if character == 'l':
        break
    print(character)