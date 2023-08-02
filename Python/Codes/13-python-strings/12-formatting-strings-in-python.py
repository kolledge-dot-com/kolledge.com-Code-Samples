name = "John"
age = 25
message = "My name is %s and I am %d years old." % (name, age)
print(message)

name = "Mary"
age = 30
message = "My name is {} and I am {} years old.".format(name, age)
print(message)


name = "Lucy"
age = 35
message = f"My name is {name} and I am {age} years old."
print(message)


info = {'name': 'Peter', 'age': 40}
message = "{name} is {age} years old.".format_map(info)
print(message)



from string import Template

name = "Sarah"
age = 33
t = Template("$name is $age years old.")
message = t.substitute(name=name, age=age)
print(message)