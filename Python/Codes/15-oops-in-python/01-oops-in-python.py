# Defining a  class in Python :
class Employee:
    company_address = "12th street"

    # state - initializing data members
    def __init__(self, name, id, desig):
        # data members (instance variables)
        self.name = name
        self.id = id
        self.desig = desig

    # Behavior (instance methods)
    def calculate_salary(self):
        # Code to calculate salary
        pass



    # Behavior (instance methods)
    def record_attendance(self):
        # Code to record attendance
        pass



# Creating an object of the class - Instantiating the class
steve = Employee('Steve', 1203, 'Project Manager')
