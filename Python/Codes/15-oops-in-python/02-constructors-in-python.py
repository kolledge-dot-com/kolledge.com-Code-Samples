# super() function :
class Animal:
    def __init__(self, type):
        self.type = type


class Dog(Animal):
    def __init__(self, name):
        self.name = name
        super().__init__("Dog")


d = Dog("Bruzo")
print(f"Type of Animal = {d.type}")
print(f"Name of {d.type} is {d.name} ")
