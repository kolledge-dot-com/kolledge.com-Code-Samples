# append to a file in Python
file = open("example.txt", "a")
file.write("This line will be appended to the file.")
file.close()




# append and read on the same File
with open("example.txt", "a+") as file:
 file.write("This line will be appended to the file.\n")
 file.seek(0)
 contents = file.read()
print(contents)




# Writing to a Binary File
with open("example.bin", "ab") as file:
 file.write(b"\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21")