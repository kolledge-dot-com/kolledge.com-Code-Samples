# Default parameters

# Defining function area_triangle
def area_triangle(base, height=10):
    area = 0.5 * (base * height)
    return area


b = 4
h = 20

# calling the function area_triangle without height
# default value of height will be used
ar = area_triangle(b)
print("The area of triangle is : ", ar)

print()

# calling the function area_triangle with height
ar = area_triangle(b, h)
print("The area of triangle is : ", ar)