# Accessing class variables :
class Employee:
    company_name = "ABC Inc."

    def __init__(self, emp_name, emp_id, emp_desig):
        self.name = emp_name
        self.id = emp_id
        self.desig = emp_desig
        self.cname = Employee.company_name  # Accessing class variable using class name

    def print_details(self):
        print(f"Name of employee = {self.name}")
        print(f"ID of employee = {self.id}")
        print(f"Designation of employee = {self.desig}")
        print(f"Company of employee = {self.company_name}")  # Accessing class variable using self keyword
        print()


# Creating objects
emp_1 = Employee("Steve", "k2591", "Manager")
emp_2 = Employee("Rob", "k2586", "Tech Lead")

# Accessing class variable outside the class
# using class name
cmp_name = Employee.company_name
print(f"Employee details for {cmp_name}")
print()

emp_1.print_details()
emp_2.print_details()


# Accessing class variable outside the class
# using object name
emp_1_cname = emp_1.company_name
print(f"Company name for Employee 1 = {emp_1_cname}")






# Modifying the class variables :
class Employee:
    company_name = "ABC Inc."

    def __init__(self, emp_name, emp_id, emp_desig):
        self.name = emp_name
        self.id = emp_id
        self.desig = emp_desig

    def print_details(self):
        print(f"Name of employee = {self.name}")
        print(f"ID of employee = {self.id}")
        print(f"Designation of employee = {self.desig}")
        print(f"Company of employee = {self.company_name}")
        print()


emp_1 = Employee("Steve", "k2591", "Manager")

# Printing initial details :
print(f"Initial Employee details for {Employee.company_name}")
print()
emp_1.print_details()


# Modifying class variable
Employee.company_name = "XYZ Inc."


# Printing modified details :
print(f"Modified Employee details for {Employee.company_name}")
print()
emp_1.print_details()





# Class variables in case of inheritance :
class Employee:
    company_name = "ABC Inc."

    def __init__(self, emp_name, emp_id, emp_desig):
        self.name = emp_name
        self.id = emp_id
        self.desig = emp_desig


class ContractEmployees(Employee):
    contract_term = "6 months"

    def print_details(self):
        print(f"Name of employee = {self.name}")
        print(f"ID of employee = {self.id}")
        print(f"Designation of employee = {self.desig}")
        print(f"Company of employee = {self.company_name}")
        print(f"Contract Term = {self.contract_term}")
        print()


emp_1 = ContractEmployees("Steve", "k2591", "Manager")
emp_1.print_details()

# Changing class variable of Parent class
# using child class name
ContractEmployees.company_name = "ABC Contract Inc."
emp_1.print_details()