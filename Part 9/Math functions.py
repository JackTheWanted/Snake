# Define a simple function that prints x
def f(x):
    x += 1
    print(x)
    
# Set y
x = 10
# Call the function
f(x)
# Print y to see if it changed
print(x)

def volume_sphere(radius):
    pi = 3.141592653589
    volume = (4 / 3) * pi * radius ** 3
    print("The volume is", volume)

def volume_cylinder(radius, height):
    pi = 3.141592653589
    volume = pi * radius ** 2 * height
    print("The volume is", volume)
    return volume

def sum_two_numbers(a, b):
    result = a + b
    return result