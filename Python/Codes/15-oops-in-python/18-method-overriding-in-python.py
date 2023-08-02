# Example: Method Overriding
class Animal:
   def speak(self):
       print("This animal speaks.")

class Dog(Animal):
   def speak(self):
       print("This dog barks.")

class Cat(Animal):
   def speak(self):
       print("This cat meows.")

a = Animal()
a.speak()
# Output: This animal speaks.

d = Dog()
d.speak()
# Output: This dog barks.

c = Cat()
c.speak()