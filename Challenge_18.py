num=int(input("enter a number:"))

if 10<num<20:
    print("Correct")
elif num<10:
    print("TOO LOW")
elif num>20:
    print("TOO HIGH")
else:
    if num==10:
        print("TOO LOW")
    if num==20:
        print("TOO HIGH")