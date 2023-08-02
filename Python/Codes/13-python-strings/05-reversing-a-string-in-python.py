# Reverse a string in Python using a loop:
my_string = "Hello, world!"
reversed_string = ""
for i in range(len(my_string) - 1, -1, -1):
    reversed_string += my_string[i]
print(reversed_string)




# Reverse a string in Python using recursion:
def reverse_string(string):
    if len(string) == 0:
        return string
    else:
        return reverse_string(string[1:]) + string[0]


my_string = "Hello, world!"
print(reverse_string(my_string))





# Reverse string in Python using stack:
my_string = "Hello, world!"

stack = []
for character in my_string:
    stack.append(character)
reversed_string = ""

# Popping characters one by one from stack
while len(stack) > 0:
    reversed_string += stack.pop()
print(reversed_string)




# Reverse string in Python using an extended slice:
my_string = "Hello, world!"
reversed_string = my_string[::-1]
print(reversed_string)




# Reverse string in Python using reversed() method :
my_string = "Hello, world!"
reversed_string = ''.join(reversed(my_string))
print(reversed_string)




# Reverse string in Python using list comprehension :
my_string = "Hello, world!"
reversed_string = ''.join([my_string[index] for index in range(len(my_string) - 1, -1, -1)])
print(reversed_string)




# Reverse string in Python using join function :
my_string = "Hello, world!"
reversed_string = ''.join(reversed(list(my_string)))
print(reversed_string)