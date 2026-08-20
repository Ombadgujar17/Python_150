num=int(input(''' 1)SQUARE\n 2)TRIANGLE\n Enter the Number: '''))

if num==1:
    length=int(input("Enter length of square: "))
    area=length**2
    print("Area of the Square is:",area)
elif num==2:
    base=int(input("Enter base of triangle: "))
    height=int(input("Enter height of triangle: "))
    area=0.5*base*height
    print("Area of the triangle is: ",area)
else:
    print("Enter a valid input(1 or 2)")