# Public data members in Python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


car = Car("Audi", "Q7", 2023)

# Accessing data members from outside the class
print(f"The make of the car is : {car.make}")
print(f"The model of the car is : {car.model}")
print(f"The year of the car is : {car.year}")




# Private data members in Python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.__year = year

    def show_year(self):
        print()
        print("Printing the year from within the class")
        print(f"The year of the car is : {self.__year}")
        print()


car = Car("Audi", "Q7", 2023)
car.show_year()

# Accessing data members from outside the class
print(f"The make of the car is : {car.make}")
print(f"The model of the car is : {car.model}")
print(f"The year of the car is : {car.__year}")




# Protected data members in Python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self._year = year

    def show_year(self):
        print()
        print("Printing the year from within the class")
        print(f"The year of the car is : {self._year}")
        print()


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)


car = Car("Audi", "Q7", 2023)
car.show_year()

# Accessing data members from inherited class
ecar = ElectricCar("Audi", "Q7", 2023)
print(f"The year of the e-car = {ecar._year}")
print()

# Accessing data members from outside code
print(f"The year of the car = {car._year}")




# Name mangling in Python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.__year = year



car = Car("Audi", "Q7", 2023)

# Accessing data members from outside the class
yr = _Car__year
print(f"The year of the car is : {yr}")
