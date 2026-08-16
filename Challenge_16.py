user=input("Is it Raining? ")
user=user.lower()

if user=="yes":
    wind=input("Is it Windy? ")
    wind.lower()
    if wind=='yes':
        print("It is too windy for an Umberalla")
    else:
        print("Take an Umberalla")
else:
    print("Enjoy you Day!")