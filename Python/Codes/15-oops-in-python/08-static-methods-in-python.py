# using the @staticmethod decorator
class Employee:
    def __init__(self, emp_name, emp_id, emp_desig):
        self.name = emp_name
        self.id = emp_id
        self.desig = emp_desig

    @staticmethod
    def show_company(cmp_name):
        print(f"The name of the company is : {cmp_name}")

    def print_details(self):
        print(f"Name of employee = {self.name}")
        print(f"ID of employee = {self.id}")
        print(f"Designation of employee = {self.desig}")
        print()


emp_1 = Employee("Steve", "k2591", "Manager")
emp_1.print_details()

# Calling the static method
Employee.show_company("ABC Inc.")






# using the staticmethod() function
class Employee:
    def __init__(self, emp_name, emp_id, emp_desig):
        # data members (instance variables  - name, id and desig)
        self.name = emp_name
        self.id = emp_id
        self.desig = emp_desig

    def show_company(cmp_name):
        print(f"The name of the company is : {cmp_name}")

    def print_details(self):
        print(f"Name of employee = {self.name}")
        print(f"ID of employee = {self.id}")
        print(f"Designation of employee = {self.desig}")
        print()


emp_1 = Employee("Steve", "k2591", "Manager")
emp_1.print_details()

# Creating a static method
Employee.show_company = staticmethod(Employee.show_company)

# Calling the static method
Employee.show_company("ABC Inc.")





# Accessing a static method
class Employee:
    def __init__(self, emp_name, emp_id, emp_desig):
        self.name = emp_name
        self.id = emp_id
        self.desig = emp_desig

    @staticmethod
    def show_company(cmp_name):
        print(f"The name of the company is : {cmp_name}")
        print()


emp_1 = Employee("Steve", "k2591", "Manager")

# Calling the static method using class name
Employee.show_company("ABC Inc.")

# Calling the static method using object name
emp_1.show_company("ABC Inc.")



