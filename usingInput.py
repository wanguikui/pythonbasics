

myDbValues=("sekina","123")

# Using input
un=input("Enter your username: ")
psw=input("Enter your password: ")

if un=="sekina" and  psw=="123":
    print("login")
else:
    print("enter correct details")

# You can also use
un=input("Enter your username: ")
psw=input("Enter your password: ")

if un==myDbValues[0] and psw==[1]:
    print("login")
else:
    print("enter correct details")


# print(un)
# print(psw)