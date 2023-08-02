# write a row to a CSV file
import csv

# Writing to a csv file
with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age'])
    writer.writerow(['John', '26'])




# Writing multiple rows to CSV Files in Python
import csv

# Writing multiple rows to a csv file example
rows = [['Name', 'Age'], ['John', '26'], ['Jane', '24']]
with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)




# write to CSV Files using the DictWriter Class
import csv

# Writing to a csv file as a dictionary
rows = [{'Name': 'John', 'Age': '26'}, {'Name': 'Jane', 'Age': '24'}]

with open('data.csv', mode='w', newline='') as file:
   fieldnames = ['Name', 'Age']
   writer = csv.DictWriter(file, fieldnames=fieldnames)
   writer.writeheader()  # Write header row
   writer.writerows(rows)  # Write rows