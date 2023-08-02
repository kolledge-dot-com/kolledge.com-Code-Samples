# Establishing a Connection
import mysql.connector

mydb = mysql.connector.connect(
 host="localhost",
 user="yourusername",
 password="yourpassword"
)

print(mydb)




# Creating and Executing SQL Queries
import mysql.connector

mydb = mysql.connector.connect(
 host="localhost",
 user="yourusername",
 password="yourpassword",
 database="mydatabase"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()

for x in myresult:
 print(x)




 # Executing CRUD Operations
 import mysql.connector

 mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
 )
 mycursor = mydb.cursor()

 # Create
 sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
 val = ("John", "Highway 21")
 mycursor.execute(sql, val)
 mydb.commit()

 # Read
 mycursor.execute("SELECT * FROM customers")
 myresult = mycursor.fetchall()
 for x in myresult:
  print(x)

 # Update
 sql = "UPDATE customers SET address = 'Canyon 123' WHERE name = 'John'"
 mycursor.execute(sql)
 mydb.commit()

 # Delete
 sql = "DELETE FROM customers WHERE name = 'John'"
 mycursor.execute(sql)
 mydb.commit()