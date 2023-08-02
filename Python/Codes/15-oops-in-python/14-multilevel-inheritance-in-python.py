# Creating a Subclass with Multilevel Inheritance
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

class Bulldog(Dog):
   def __init__(self, name):
       super().__init__(name, "Bulldog")
   def speak(self):
       super().speak()
       print("This Bulldog growls")

b = Bulldog("Buddy")
b.speak()