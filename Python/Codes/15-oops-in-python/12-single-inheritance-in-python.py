# Code sample for single inheritance
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model


class Car(Vehicle):
    def __init__(self, make, model, utility, transmission):
        self.utility = utility
        self.transmission = transmission
        super().__init__(make, model)

    def show_details(self):
        print(f"The make of the Car is : {self.make}")
        print(f"The model of the Car is : {self.model}")
        print(f"The utility of the Car is : {self.utility}")
        print(f"The transmission of the Car is : {self.transmission}")


my_car = Car("Audi", 2023, "SUV", "Automatic")
my_car.show_details()





# Overriding methods :
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def show_details(self):
        print(f"The make of the Vehicle  is : {self.make}")
        print(f"The model of the Vehicle is : {self.model}")
        print()


class Car(Vehicle):
    def __init__(self, make, model, utility, transmission):
        self.utility = utility
        self.transmission = transmission
        super().__init__(make, model)

    # Overriding method of the super class
    def show_details(self):
        print(f"The make of the Car is : {self.make}")
        print(f"The model of the Car is : {self.model}")
        print(f"The utility of the Car is : {self.utility}")
        print(f"The transmission of the Car is : {self.transmission}")
        print()


my_vehicle = Vehicle("BMW", 2022)
my_car = Car("Audi", 2023, "SUV", "Automatic")

# Calling show_details method of super class
my_vehicle.show_details()

# Calling show_details method of sub class
my_car.show_details()




# Accessing super-class methods :
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def show_details(self):
        print(f"The make of the Vehicle  is : {self.make}")
        print(f"The model of the Vehicle is : {self.model}")
        print()


class Car(Vehicle):
    def __init__(self, make, model, utility, transmission):
        self.utility = utility
        self.transmission = transmission
        super().__init__(make, model)

    # Overriding method of the super class
    def show_details(self):
        # Calling show_details method of super class
        super().show_details()

        print(f"The utility of the Car is : {self.utility}")
        print(f"The transmission of the Car is : {self.transmission}")
        print()


my_car = Car("Audi", 2023, "SUV", "Automatic")
my_car.show_details()