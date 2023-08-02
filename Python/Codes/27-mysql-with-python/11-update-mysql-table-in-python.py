# Update table
query = "UPDATE employees SET name = %s WHERE id = %s"
values = ("Jane", 1)
cursor.execute(query, values)