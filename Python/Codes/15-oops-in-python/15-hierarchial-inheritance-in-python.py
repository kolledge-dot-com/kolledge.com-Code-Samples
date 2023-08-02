# Creating Subclasses with Hierarchical Inheritance
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

d = Dog("Buddy", "Bulldog")
d.speak()

# Output: This dog barks

c = Cat("Kitty", "Persian")
c.speak()