# Example of python immutable Objects :
a = 5
b = a           # b is assigned the value of a
a = a + 1       # a is incremented, but b remains unchanged
print(a)        # Output: 6
print(b)        # Output: 5





name = "John"
new_name = name.upper()      # upper() method returns a new string
print(name)                 # Output: John
print(new_name)             # Output: JOHN





# Example of Python mutable Objects :
students = ['John', 'Amy', 'Mike']
students.append('Sarah')        # 'Sarah' added to end of list
print(students)                # Output: ['John', 'Amy', 'Mike', 'Sarah']
grades = {'John': 90, 'Amy': 85, 'Mike': 95}
grades['John'] = 95             # 'John' grade updated to 95
print(grades)                   # Output: {'John': 95, 'Amy': 85, 'Mike': 95}




# Passing Arguments to Python Functions
def double(num):
   num = num * 2            # num is a local copy, original value outside the function is not changed
a = 5
double(a)
print(a)                     # Output: 5





def append_name(students_list):
   students_list.append('Sarah')
students = ['John', 'Amy', 'Mike']
append_name(students)
print(students)              # Output: ['John', 'Amy', 'Mike', 'Sarah']
