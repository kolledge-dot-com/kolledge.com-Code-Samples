# Delete data from table
query = "DELETE FROM employees WHERE id = %s"
values = (1,)
cursor.execute(query, values)