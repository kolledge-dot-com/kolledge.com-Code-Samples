# write to a text file in python
file = open("example.txt", "w")
file.write("Hello, world!")
file.close()



# write() Method :
file = open("example.txt", "w")
file.write("This is a line of text.")
file.close()




# writelines() Method :
list_of_lines = ["This is line 1.", "This is line 2.", "This is line 3."]
with open("example.txt", "w") as file:
 	file.writelines(list_of_lines)



# Using with statement to write a file :
with open("example.txt", "w") as file:
 	file.write("This is a line of text.")




# write to a binary file in python :
with open("example.bin", "wb") as file:
 file.write(b"\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21")