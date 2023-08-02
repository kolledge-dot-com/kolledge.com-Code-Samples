# using instance methods
class Employee:
    def __init__(self, emp_name, emp_id, emp_desig, basic_salary):
        # data members (instance variables  - name, id and desig)
        self.name = emp_name
        self.id = emp_id
        self.desig = emp_desig
        self.basic_sal = basic_salary

    def calc_salary(self, incr_rate):
        self.salary = self.basic_sal + self.basic_sal * incr_rate

    def print_details(self):
        print(f"Name of employee = {self.name}")
        print(f"ID of employee = {self.id}")
        print(f"Designation of employee = {self.desig}")
        print(f"Salary of employee = {self.salary}")
        print()


# Creating Employee objects
emp_1 = Employee("Steve", "k2591", "Manager", 50000)
emp_2 = Employee("Rob", "k2586", "Tech Lead", 40000)

# Calculating Salary for the Employees
emp_1.calc_salary(5.2)
emp_2.calc_salary(4.5)

# Printing details for employees
emp_1.print_details()
emp_2.print_details()





# Add new instance method dynamically
import types

class Employee:
    def __init__(self, emp_name, emp_id, emp_desig):
        # data members (instance variables  - name, id and desig)
        self.name = emp_name
        self.id = emp_id
        self.desig = emp_desig

    def print_details(self):
        print(f"Name of employee = {self.name}")
        print(f"ID of employee = {self.id}")
        print(f"Designation of employee = {self.desig}")
        print()


emp_1 = Employee("Steve", "k2591", "Manager")
emp_1.print_details()


# Defining the function that we want to add to object
def communicate(self, email):
    print(f"Email Id of employee : ", email)


# Adding the function to the object emp_1
emp_1.communicate = types.MethodType(communicate, emp_1)

# Calling the newly added function
emp_1.communicate("abc@xyz.com")






# Deleting instance methods dynamically Using del keyword
class Employee:
    def __init__(self, emp_name, emp_id, emp_desig, basic_salary):
        # data members (instance variables  - name, id and desig)
        self.name = emp_name
        self.id = emp_id
        self.desig = emp_desig
        self.basic_sal = basic_salary

    def calc_salary(self, incr_rate):
        self.salary = self.basic_sal + self.basic_sal * incr_rate

    def print_details(self):
        print(f"Name of employee = {self.name}")
        print(f"ID of employee = {self.id}")
        print(f"Designation of employee = {self.desig}")
        print(f"Salary of employee = {self.salary}")
        print()


emp_1 = Employee("Steve", "k2591", "Manager", 50000)
del emp_1.calc_salary
emp_1.calc_salary(5.2)





# Deleting instance methods dynamically Using delattr() function
class Employee:
    def __init__(self, emp_name, emp_id, emp_desig, basic_salary):
        # data members (instance variables  - name, id and desig)
        self.name = emp_name
        self.id = emp_id
        self.desig = emp_desig
        self.basic_sal = basic_salary

    def calc_salary(self, incr_rate):
        self.salary = self.basic_sal + self.basic_sal * incr_rate

    def print_details(self):
        print(f"Name of employee = {self.name}")
        print(f"ID of employee = {self.id}")
        print(f"Designation of employee = {self.desig}")
        print(f"Salary of employee = {self.salary}")
        print()


emp_1 = Employee("Steve", "k2591", "Manager", 50000)
# del emp_1.calc_salary
delattr(emp_1, "calc_salary")
emp_1.calc_salary(5.2)