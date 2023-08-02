# Using the + Operator :
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)




# Using the join() Method :
my_list = ["Hello", "World"]
separator = " "
result = separator.join(my_list)
print(result)




# Using f-strings :
name = "Alice"
age = 30
result = f"My name is {name} and I am {age} years old."
print(result)




# Using the format() Method :
str1 = "Hello"
str2 = "World"
result = "{} {}".format(str1, str2)
print(result)




# Using the % Formatting :
str1 = "Hello"
str2 = "World"
result = "%s %s" % (str1, str2)
print(result)




# Using String Slicing :
str1 = "Hello"
str2 = "Kolledge"
result = str1 + " " +str2[4:]
print(result)



# Concatenating Strings with Non-Strings :
num1 = 10
num2 = 5.5
str1 = "The result is: "
result = str1 + str(num1 + num2)
print(result)
