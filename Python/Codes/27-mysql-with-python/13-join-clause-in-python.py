# use sql join clause
query = "SELECT employees.name, departments.department_name FROM employees JOIN departments ON employees.department_id = departments.id"
cursor.execute(query)
result = cursor.fetchall()
for row in result:
   print(row)