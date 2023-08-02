# Method Overriding:
class Animal:
    def speak(self):
        print("Animal speaks")


class Dog(Animal):
    def speak(self):
        print("Dog barks")


class Cat(Animal):
    def speak(self):
        print("Cat meows")


a = Animal()
a.speak()

d = Dog()
d.speak()

c = Cat()
c.speak()





# Method Overloading using default arguments :
class Calculator:
    def add(self, x, y, z=0):
        return x + y + z


c = Calculator()

sum_2 = c.add(6, 7)
sum_3 = c.add(2, 3, 4)

print(f"The sum of three numbers = {sum_3}")
print(f"The sum of two numbers = {sum_2}")




# Method Overloading using variadic functions :
class Calculator:
    def add(self, x, y, *args):
        l = len(args)
        if l > 0:
            return x + y + args[0]
        else:
            return x + y


c = Calculator()

sum_2 = c.add(6, 7)
sum_3 = c.add(2, 3, 4)

print(f"The sum of three numbers = {sum_3}")
print(f"The sum of two numbers = {sum_2}")




# Method Overloading using keyword arguments :
class Calculator:
    def add(self, x, y, **kwargs):
        if 'z' in kwargs:
            return x + y + kwargs["z"]
        else:
            return x + y


c = Calculator()

sum_2 = c.add(x=6, y=7)
sum_3 = c.add(x=2, y=3, z=4)

print(f"The sum of three numbers = {sum_3}")
print(f"The sum of two numbers = {sum_2}")




# Method Overloading using dispatch decorator :
from multipledispatch import dispatch


@dispatch(int, int)
def add(num_1, num_2):
    result = num_1 + num_2
    return result


@dispatch(int, int, int)
def add(num_1, num_2, num_3):
    result = num_1 + num_2 + num_3
    return result


@dispatch(float, float, float)
def add(num_1, num_2, num_3):
    result = num_1 + num_2 + num_3
    return result


# calling product method with 2 arguments
res = add(5, 4)
print(f"The sum of two numbers = {res}")

# calling product method with 3 arguments but all int
res = add(5, 4, 2)
print(f"The sum of three numbers = {res}")

# calling product method with 3 arguments but all float
res = add(5.1, 4.31, 2.6)
print(f"The sum of three float numbers = {res}")




# Duck Typing :
class Duck:
    def quack(self):
        print("Quack quack")


class Person:
    def quack(self):
        print("I can't quack like a duck, but I can mimic it")


def duck_quack(obj):
    obj.quack()


d = Duck()
p = Person()

# Both the Duck and Person objects can be passed to the duck_quack() function
duck_quack(d)
duck_quack(p)




# Operator Overloading :
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2
print(v3.x, v3.y)