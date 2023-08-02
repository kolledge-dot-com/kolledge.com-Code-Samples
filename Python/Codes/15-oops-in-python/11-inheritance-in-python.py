# Accessing Super-class Methods :
class Employee:
    def __init__(self, emp_name, emp_id, emp_desig):
        self.name = emp_name
        self.id = emp_id
        self.desig = emp_desig

    def show_details(self):
        print(f"The name of the Employee is : {self.name}")
        print(f"The id of the Employee is : {self.id}")
        print(f"The desig of the Employee is : {self.desig}")


class ContractEmployees(Employee):
    def __init__(self, emp_name, emp_id, emp_desig, contract_term):
        self.term = contract_term

        # Calling constructor of parent class
        super().__init__(emp_name, emp_id, emp_desig)

    def emp_details(self):
        # Calling show_details function of parent class
        super().show_details()

        print(f"The contract term of the Employee is : {self.term}")


emp = ContractEmployees("John", "2k1023", "Tech Asst.", "6 Months")
emp.emp_details()




# Overriding Methods :
class Employee:
    def __init__(self, emp_name, emp_id, emp_desig):
        self.name = emp_name
        self.id = emp_id
        self.desig = emp_desig

    def show_details(self):
        print(f"The name of the Employee is : {self.name}")
        print(f"The id of the Employee is : {self.id}")
        print(f"The desig of the Employee is : {self.desig}")


class ContractEmployees(Employee):
    def __init__(self, emp_name, emp_id, emp_desig, contract_term):
        self.term = contract_term

        # Calling constructor of parent class
        super().__init__(emp_name, emp_id, emp_desig)

    # Overriding method of the parent class
    def show_details(self):
        # Calling show_details function of parent class
        super().show_details()

        print(f"The contract term of the Employee is : {self.term}")


emp = ContractEmployees("John", "2k1023", "Tech Asst.", "6 Months")

# The method from the child class will be called
emp.show_details()




# Inheriting from Multiple classes

class Employee:
    # Code for super-class Employee
    pass

class Contract:
    # Code for super-class Contract
    pass

class ContractEmployees(Employee, Contract):
    # Code for sub-class ContractEmployees
    pass