# Embedding variables within f-strings
x = 10
my_str = f"The value of x = {x}"
print(my_str)



# Embedding expressions within f-strings
x = 10
y = 20
my_str = f"The sum of {x} and {y} = {x + y}"
print(my_str)



# Embedding function calls within f-strings
def avrg(a, b):
    return (a + b) / 2


x = 10
y = 20
my_str = f"The average of {x} and {y} = {avrg(x, y)}"
print(my_str)




# Multiline f-string
def avrg(a, b):
    return (a + b) / 2


x = 10
y = 20

my_str = f'''The sum of {x} and {y} = {x + y}
The average of {x} and {y} = {avrg(x, y)}'''

print(my_str)



# Embedding braces within f-strings
name = "World"
f_str = f"Embracing the :  {{ {name} }} "
print(f_str)
