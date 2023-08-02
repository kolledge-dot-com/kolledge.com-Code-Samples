# Insert Values in MySQL Table
query = "INSERT INTO employees (id, name) VALUES (1, 'John')"
cursor.execute(query)

#Print message to confirm Inserting Values
print("Values Inserted successfully!")