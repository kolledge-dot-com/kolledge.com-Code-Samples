# Calling a Method of the Superclass That Has Been Overridden in the Subclass
class Animal:
   def speak(self):
       print("This animal speaks")

class Dog(Animal):
   def speak(self):
       print("This dog barks")
d = Dog()
d.speak()           # Output: This dog barks

class Bulldog(Dog):
   def speak(self):
       print("This Bulldog growls")
b = Bulldog()
b.speak()           # Output: This Bulldog growls

class Pug(Dog):
   def speak(self):
       super().speak()
       print("This Pug snorts")

p = Pug()
p.speak()