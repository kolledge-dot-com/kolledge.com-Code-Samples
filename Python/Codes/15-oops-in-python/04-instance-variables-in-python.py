# Using the object name and dot operator :
class Employee:
    def __init__(self, emp_name, emp_id, emp_desig):
        # data members (instance variables  - name, id and desig)
        self.name = emp_name
        self.id = emp_id
        self.desig = emp_desig


# Employee 1 object
emp_1 = Employee("Steve", "k2591", "Manager")


# Accessing instance variables for employee 1
# Using object_name and dot operator
employee_name = emp_1.name
employee_id = emp_1.id
employee_desig = emp_1.desig

# Printing details for employee 1
print(f"Name of employee = {employee_name}")
print(f"ID of employee = {employee_id}")
print(f"Designation of employee = {employee_desig}")
print()




# Using the self keyword and dot operator :
class Employee:
    def __init__(self, emp_name, emp_id, emp_desig):
        # data members (instance variables  - name, id and desig)
        self.name = emp_name
        self.id = emp_id
        self.desig = emp_desig

    # Instance method
    def print_details(self):
    	# Accessing instance variables for employees
		# Using self keyword and dot operator
        print(f"Name of employee = {self.name}")
        print(f"ID of employee = {self.id}")
        print(f"Designation of employee = {self.desig}")


# Employee 1
emp_1 = Employee("Steve", "k2591", "Manager")
emp_1.print_details()
print()

# Employee 2
emp_2 = Employee("Rob", "k2586", "Tech Lead")
emp_2.print_details()




# Using the getattr() method :
class Employee:
    def __init__(self, emp_name, emp_id, emp_desig):
        # data members (instance variables  - name, id and desig)
        self.name = emp_name
        self.id = emp_id
        self.desig = emp_desig


# Employee 1 object
emp_1 = Employee("Steve", "k2591", "Manager")


# Accessing instance variables for employee 1
# Using getattr method and dot operator
employee_name = getattr(emp_1,'name')
employee_id = getattr(emp_1,'id')
employee_desig = getattr(emp_1,'desig')

# Printing details for employee 1
print(f"Name of employee = {employee_name}")
print(f"ID of employee = {employee_id}")
print(f"Designation of employee = {employee_desig}")
print()






# Modifying instance variables :

# Using the object name and dot operator
class Employee:
    def __init__(self, emp_name, emp_id, emp_desig):
        # data members (instance variables  - name, id and desig)
        self.name = emp_name
        self.id = emp_id
        self.desig = emp_desig


# Employee 1 object
emp_1 = Employee("Steve", "k2591", "Manager")

# Printing Initial details for employee 1
print(f"Name of employee = {emp_1.name}")
print(f"ID of employee = {emp_1.id}")
print(f"Designation of employee = {emp_1.desig}")
print()

# Modifying the value of desig instance variable
emp_1.desig = "Sr. Manager"

# Printing Modified details for employee 1
print(f"Name of employee = {emp_1.name}")
print(f"ID of employee = {emp_1.id}")
print(f"Designation of employee = {emp_1.desig}")
print()



# using the self keyword and dot operator
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

    def modify_designation(self,new_value):
        # Modifying the value of desig instance variable
        # Using self keyword
        self.desig = new_value


# Employee 1 object
emp_1 = Employee("Steve", "k2591", "Manager")

# Printing Initial details for employee 1
emp_1.print_details()


emp_1.modify_designation("Sr. Manager")

# Printing Modified details for employee 1
emp_1.print_details()



# Using the setattr() Method :
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

# Employee 1 object
emp_1 = Employee("Steve", "k2591", "Manager")

# Printing Initial details for employee 1
emp_1.print_details()

# Modifying the value of desig instance variable
# Using setattr method
setattr(emp_1,"desig","Sr. Manager")

# Printing Modified details for employee 1
emp_1.print_details()





# Fetching Instance variables using __dict__ function :

class Employee:
    def __init__(self, emp_name, emp_id, emp_desig):
        # data members (instance variables  - name, id and desig)
        self.name = emp_name
        self.id = emp_id
        self.desig = emp_desig


emp_1 = Employee("Steve", "k2591", "Manager")
inst_variables = emp_1.__dict__
print(inst_variables)





# Adding instance variables dynamically
class Employee:
    def __init__(self, emp_name, emp_id, emp_desig):
        # data members (instance variables  - name, id and desig)
        self.name = emp_name
        self.id = emp_id
        self.desig = emp_desig


emp_1 = Employee("Steve", "k2591", "Manager")
emp_2 = Employee("Rob", "k2586", "Tech Lead")

print(emp_1.__dict__)  # Print initial details of employee 1
print(emp_2.__dict__)  # Print initial details of employee 2
print()

emp_1.email = "steve@mail.com"  # Add new instance variable to employee 1

print(emp_1.__dict__)  # Print new details of employee 1
print(emp_2.__dict__)  # Print new details of employee 2





# Deleting instance variables dynamically

# Using del keyword :
class Employee:
    def __init__(self, emp_name, emp_id, emp_desig):
        # data members (instance variables  - name, id and desig)
        self.name = emp_name
        self.id = emp_id
        self.desig = emp_desig


emp_1 = Employee("Steve", "k2591", "Manager")
emp_2 = Employee("Rob", "k2586", "Tech Lead")

print(emp_1.__dict__)  # Print initial details of employee 1
print(emp_2.__dict__)  # Print initial details of employee 2
print()

del emp_1.desig  # Delete instance variable desig of employee 1

print(emp_1.__dict__)  # Print new details of employee 1
print(emp_2.__dict__)  # Print new details of employee 2



# Using delattr() function :
class Employee:
    def __init__(self, emp_name, emp_id, emp_desig):
        # data members (instance variables  - name, id and desig)
        self.name = emp_name
        self.id = emp_id
        self.desig = emp_desig


emp_1 = Employee("Steve", "k2591", "Manager")
emp_2 = Employee("Rob", "k2586", "Tech Lead")

print(emp_1.__dict__)  # Print initial details of employee 1
print(emp_2.__dict__)  # Print initial details of employee 2
print()

delattr(emp_1, "desig")   # Delete instance variable desig of employee 1

print(emp_1.__dict__)  # Print new details of employee 1
print(emp_2.__dict__)  # Print new details of employee 2