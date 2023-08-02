# Memoryview in Python
obj = bytearray('Kolledge','utf-8')
m = memoryview(obj)

print("Data type of m : ", type(m))
print(m[0])
print(bytes(m[0:3]))