num1=int(input("Enter a number above 100: "))
if num1<100:
    print("Did i told you to enter number lower than 100?")
num2=int(input("Enter a number less than 10: "))
if 0<=num2>=10:
    print("Ahhh! Enter What i said Man!!")

times=num1//num2

print(num1,"is",times,"times bigger than",num2)