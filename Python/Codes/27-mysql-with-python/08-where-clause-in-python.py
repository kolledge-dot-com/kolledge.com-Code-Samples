# Use sql where clause
query = "SELECT * FROM employees WHERE id = %s"
values = (1,)
cursor.execute(query, values)
result = cursor.fetchall()
for row in result:
   print(row)