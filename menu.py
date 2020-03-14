print("1. 20MB")
print("2. 30MB")
print("3. 40MB")

choice=int(input("Enter your choice: "))

print(type(choice))

if choice==1:
    print("You have purchased 20MB")
elif choice==2:
        print("You have purchased 30MB")
elif choice==3:
        print("You have purchased 40MB")
else:
        print("invalid")

