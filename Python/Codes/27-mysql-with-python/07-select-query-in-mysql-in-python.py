# Execute select query
query = "SELECT * FROM employees"
cursor.execute(query)
result = cursor.fetchall()
for row in result:
   print(row)