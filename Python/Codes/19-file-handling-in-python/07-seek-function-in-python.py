# Example code for using seek() function
file = open("example.txt", "r")

# move file handle to position 10
file.seek(10)

# read from position 10 to the end of file
print(file.read())


file.close()

