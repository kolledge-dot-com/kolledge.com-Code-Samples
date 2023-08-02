# String Concatenation
string1 = "Hello"
string2 = "world"
result = string1 + " " + string2
print(result)



# String Repetition
string = "Hello-"
result = string * 3
print(result)



# String Slicing
string = "Hello world"
result = string[0:5]
print(result)



# String Length
string = "Hello world"
result = len(string)
print(result)


# String Case Conversion
string = "Hello world"
result1 = string.upper()
result2 = string.lower()
print(result1)
print(result2)



# String Strip
string = "    Hello world    "
result = string.strip()
print(result)



# String Replace
string = "Hello world"
result = string.replace("world", "Kolledge Scholars")
print(result)



# String Split
string = "Hello,world"
result = string.split(",")
print(result)


# String Join
list = ['Hello', 'world']
delimiter = ","
result = delimiter.join(list)
print(result)



# String Formatting
name = "John"
age = 30
result = "My name is {} and I am {} years old".format(name, age)
print(result)