# using the @classmethod decorator
class Employee:
    company_name = "ABC Inc."

    def __init__(self, emp_name, emp_id, emp_desig):
        # data members (instance variables  - name, id and desig)
        self.name = emp_name
        self.id = emp_id
        self.desig = emp_desig

    @classmethod
    def show_company(cls):
        print(f"The name of the company is : {Employee.company_name}")

    def print_details(self):
        print(f"Name of employee = {self.name}")
        print(f"ID of employee = {self.id}")
        print(f"Designation of employee = {self.desig}")
        print()


emp_1 = Employee("Steve", "k2591", "Manager")
emp_1.print_details()
Employee.show_company()






# using the classmethod() function
class Employee:
    company_name = "ABC Inc."

    def __init__(self, emp_name, emp_id, emp_desig):
        # data members (instance variables  - name, id and desig)
        self.name = emp_name
        self.id = emp_id
        self.desig = emp_desig

    def show_company(cls):
        print(f"The name of the company is : {Employee.company_name}")

    def print_details(self):
        print(f"Name of employee = {self.name}")
        print(f"ID of employee = {self.id}")
        print(f"Designation of employee = {self.desig}")
        print()


emp_1 = Employee("Steve", "k2591", "Manager")
emp_1.print_details()

Employee.show_company = classmethod(Employee.show_company)
Employee.show_company()





# Add new class method dynamically
class Employee:
    company_name = "ABC Inc."

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


# Function that will be added to class
def show_company(cls):
    print(f"The name of the company is : {Employee.company_name}")


# Adding the class method dynamically
Employee.show_company = classmethod(show_company)

emp_1 = Employee("Steve", "k2591", "Manager")
Employee.show_company()  # Calling the class method added dynamically
emp_1.print_details()





# Deleting class methods dynamically Using del keyword
class Employee:
    company_name = "ABC Inc."

    def __init__(self, emp_name, emp_id, emp_desig):
        # data members (instance variables  - name, id and desig)
        self.name = emp_name
        self.id = emp_id
        self.desig = emp_desig

    @classmethod
    def show_company(cls):
        print(f"The name of the company is : {Employee.company_name}")


# Deleting the class method
del Employee.show_company

# Calling the class method added
Employee.show_company()




# Deleting class methods dynamically Using delattr() function
class Employee:
    company_name = "ABC Inc."

    def __init__(self, emp_name, emp_id, emp_desig):
        # data members (instance variables  - name, id and desig)
        self.name = emp_name
        self.id = emp_id
        self.desig = emp_desig

    @classmethod
    def show_company(cls):
        print(f"The name of the company is : {Employee.company_name}")


# Deleting the class method
delattr(Employee, "show_company")

# Calling the class method added
Employee.show_company()





# Class methods in case of inheritance
class Employee:
    company_name = "ABC Inc."

    def __init__(self, emp_name, emp_id, emp_desig):
        self.name = emp_name
        self.id = emp_id
        self.desig = emp_desig

    @classmethod
    def show_company(cls):
        print(f"The name of the company is : {Employee.company_name}")


class ContractEmployees(Employee):
    contract_term = "6 months"

    def print_details(self):
        print(f"Name of employee = {self.name}")
        print(f"ID of employee = {self.id}")
        print(f"Designation of employee = {self.desig}")
        print(f"Contract Term = {self.contract_term}")
        print()


emp_1 = ContractEmployees("Steve", "k2591", "Manager")
ContractEmployees.show_company()
emp_1.print_details()