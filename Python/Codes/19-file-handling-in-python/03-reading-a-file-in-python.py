# Python read() Method
file = open("example.txt", "r")
print(file.read())
file.close()




# read N bytes from the file
with open("example.txt", "r") as file:
   bytes = file.read(10)
   print(bytes)



# Python readline() Method :
file = open("example.txt", "r")
print(file.readline())
file.close()




# read first N lines from a file using readline() :
file = open("example.txt", "r")

for i in range(15):
   print(file.readline())

file.close()




# read entire file using readline()
file = open("example.txt", "r")

while True:
    line = file.readline()
    if not line:
        break
    print(line)

file.close()




# read first and the last line using readline() :
with open("example.txt", "r") as file:
    first_line = file.readline()
    last_line = file.readlines()[-1]

print(first_line)
print(last_line)




# Python readlines() method : reading file into list
with open("example.txt", "r") as file:
   lines = file.readlines()
   for line in lines:
       print(line)



# read first N lines from a file using readlines() method :
with open("example.txt", "r") as file:
   for line in file.readlines()[:5]:
       print(line)




# read the last N lines of a file using readlines() method :
with open("example.txt", "r") as file:
   lines = file.readlines()
   for line in lines[-5:]:
       print(line)


# Reading a file using the with statement in python
with open("example.txt", "r") as file:
   print(file.read())




# Reading and Writing to the same file
with open("example.txt", "r+") as file:
   data = file.read()
   file.write("\nThis is another line.")



# Reading a binary file in Python :
with open("example.png", "rb") as file:
   data = file.read()
   print(data)



# Reading file in reverse order in python
with open("example.txt", "r") as file:
   lines = file.readlines()
   for line in reversed(lines):
       print(line.strip())