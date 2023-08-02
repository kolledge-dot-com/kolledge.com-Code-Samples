# Reading a CSV File in Python
import csv

# Reading a csv file
with open('data.csv') as file:
   reader = csv.reader(file)
   for row in reader:
       print(row)




# Reading a specific column of a CSV file
import csv

# Reading specific columns of a csv file
with open('data.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0], row[2])




# Reading a CSV File using the DictReader Class
import csv

# Reading a csv file using DictReader
with open('data.csv') as file:
   reader = csv.DictReader(file)
   for row in reader:
       print(row['Name'], row['Age'])