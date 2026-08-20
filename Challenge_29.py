import math
while True:
    num=int(input("Enter no above 500: "))
    if num<500:
        print("Enter above 500")
    else:
        square_root=math.sqrt(num)
        print(round(square_root,2))
