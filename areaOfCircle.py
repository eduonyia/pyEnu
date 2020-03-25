# Write a Python program which accepts the radius of a circle
# from the user and computes the area.

import math

radius = float(input("Enter the radius: "))

# calculate area

area = math.pi * radius * radius

print(f'Area of a circle of radius {radius} is {area}')
