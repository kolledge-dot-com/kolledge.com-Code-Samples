# Use sql orderby clause
query = "SELECT * FROM employees ORDER BY name ASC"
cursor.execute(query)
result = cursor.fetchall()
for row in result:
   print(row)