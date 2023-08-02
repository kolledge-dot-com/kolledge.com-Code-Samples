# Creating Subclasses with Hybrid Inheritance
class Animal:
   def __init__(self, species):
       self.species = species
   def speak(self):
       print("This animal speaks")

class Dog(Animal):
   def __init__(self, name, breed):
       self.name = name
       self.breed = breed
       super().__init__("Dog")
   def speak(self):
       print("This dog barks")

class Cat(Animal):
   def __init__(self, name, breed):
       self.name = name
       self.breed = breed
       super().__init__("Cat")
   def speak(self):
       print("This cat meows")

class Bulldog(Dog):
   def speak(self):
       super().speak()
       print("This Bulldog growls")

class Persian(Cat):
   def speak(self):
       super().speak()
       print("This Persian purrs")

class Pug(Bulldog, Persian):
   def __init__(self, name):
       super().__init__(name, "Pug")
   def speak(self):
       super().speak()
       print("This Pug snorts")

p = Pug("Puggy")
p.speak()