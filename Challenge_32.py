import math
radius,depth=int(input("Enter radius of cylinder: ")),int(input("Enter depth of cylinder: "))

area_of_circle=round(math.pi*(radius**2),3)
area_of_cylinder=area_of_circle*depth
print("Area of a cylinder is: ",area_of_cylinder)