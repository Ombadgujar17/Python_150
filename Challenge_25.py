first_name=input("Enter firstname: ")

if len(first_name)>5:
    last_name=input("Enter lastname: ")
    name=first_name+last_name
    print(name.upper())
else:
    print(first_name.lower())