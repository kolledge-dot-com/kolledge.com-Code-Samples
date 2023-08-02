# Connecting to MySQL using PyMySQL :
import pymysql

mydb = pymysql.connect(
   host="localhost",
   user="yourusername",
   password="yourpassword",
   database="mydatabase",
   cursorclass=pymysql.cursors.DictCursor
)

print(mydb)