# Concatenate Operator for Strings in Python
greeting = "Hello"
name = "John"
message = greeting + " " + name
print(message)

# Repetition Operator for Strings in Python
word = "hello_"
repeat_word = word * 5
print(repeat_word)


# Slicing Operator for Strings in Python:
word = "hello"
substring = word[0:3]
print(substring)



# Comparison Operator for Strings in Python
word1 = "hello"
word2 = "world"
word3 = "hello"

result = word1 == word2
result2 = word3 == word1

print(result)
print(result2)



# Membership Operator for Strings in Python:
word = "hello"
result1 = "ell" in word
result2 = "ell" not in word

print(result1)
print(result2)

result1 = "foo" in word
result2 = "foo" not in word

print(result1)
print(result2)



# Escape Sequence Operator for Strings in Python:
message = "Hello\nWorld"
print(message)



# Formatting Operator for Strings in Python:
name = "John"
age = 30
message = "My name is %s and I am %d years old." % (name, age)
print(message)