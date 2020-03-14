print("1. 20MB")
print("2. 30MB")
print("3. 40MB")

choice=(input("Enter your choice: "))

#print(type(choice))
balance=100
if choice=="1":
    if balance>=20:
        balance=balance-20
        print("You have received 20MBs")
        print("New Balance",balance)
    else:
        print("insufficient balance")

elif choice=="2":
    if balance>=30:
        balance=balance-30
        print("You have received 30MBs")
        print("New Balance",balance)
    else:
        print("insufficient balance")

if choice=="3":
    if balance>=40:
        balance=balance-40
        print("You have received 40MBs")
        print("New Balance",balance)
    else:
        print("insufficient balance")

