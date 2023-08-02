# Create table
cursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

#Print message to confirm table creation
print("Table created successfully!")


mydb.commit()

#Print message to confirm changes
print("Changes successfully saved to the database!")
