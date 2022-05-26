
import math

print("Let's do some math! \n")

square=float(input("What is the length of a side of the square in centimeters? "))
area_square=(square**2)
print(f"""The area of the square is: {area_square} cm²
The area of this square in m² is: {area_square/10000}\n""")

rectangle_length=float(input("What is the length of a rectangle in centimeters? "))
rectangle_width=float(input("What is the width of a rectangle in centimeters? "))
rectangle_area=(rectangle_length*rectangle_width)
print(f"""The area of the rectangle is: {rectangle_area} cm²
The area of this rectangle in m² is {rectangle_area/10000}\n""")

circle=float(input("What is the radius of the circle in centimeters? "))
circle_area = circle**2*math.pi
print(f"""The area of the circle is: {circle_area} cm² 
The are of this circle in m² is:{circle_area/10000}\n""")

single_value=float(input("Give us a value: "))
area_square_value=single_value**2
area_circle_value=single_value**2*math.pi
area_cube_value=single_value**3
area_sphere_value= 4*math.pi*(single_value**3)/3
print(f"""
The area of Square with the value given is: {area_square_value}
The area of a Circle with the value given is: {area_circle_value}
The area of a Cube with the value given is: {area_cube_value}
The area of a Sphere with the value given is: {area_sphere_value}""")