# Calling functions of parent class
class A:
    def show(self):
        print("Show method of parent class A")


class B:
    def show(self):
        print("Show method of parent class B")


class C(A, B):
    def display(self):
        print("Display method of class C")
        super().show()
        print()


class D(B, A):
    def display(self):
        print("Display method of class D")
        super().show()
        print()


c = C()
c.display()

d = D()
d.display()



# Invoking constructors of parent classes
class A(object):
    def __init__(self):
        print("Entering class A")
        print("Exiting class A")

class B(object):
    def __init__(self):
        print("Entering class B")
        print("Exiting class B")

class C(A, B):
    def __init__(self):
        print("Entering class C")
        A.__init__(self)
        B.__init__(self)
        print("Exiting class C")

C()




# Code Sample for multiple inheritance
# Parent Class - 1
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def show_details(self):
        print(f"The make of the Vehicle  is : {self.make}")
        print(f"The model of the Vehicle is : {self.model}")
        print()


# Parent Class - 2
class RentedVehicle:
    def __init__(self, permit_id, permit_term):
        self.permit_id = permit_id
        self.permit_term = permit_term

    def show_rent_details(self):
        print(f"The Vehicle will be used for renting purpose")
        print(f"The permit_id of the Vehicle  is : {self.permit_id}")
        print(f"The permit_term of the Vehicle is : {self.permit_term}")
        print()


# Child class
class Car(Vehicle, RentedVehicle):
    def __init__(self, make, model, utility, transmission, permit_id, permit_term):
        self.utility = utility
        self.transmission = transmission
        Vehicle.__init__(self,make, model)
        RentedVehicle.__init__(self, permit_id, permit_term)

    def show_car_details(self):
        super().show_details()
        super().show_rent_details()
        print(f"The utility of the Car is : {self.utility}")
        print(f"The transmission of the Car is : {self.transmission}")
        print()


my_car = Car("Audi", 2023, "SUV", "Automatic", "2k230101", "5 Years")
my_car.show_car_details()
