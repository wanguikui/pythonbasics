studentName=input("Enter Student Name: ")
maths=int(input("Enter your maths marks: "))
eng=int(input("Enter your English marks: "))
kisw=int(input("Enter your Kiswahili marks: "))
science=int(input("Enter your science marks: "))
sst=int(input("input your SST marks: "))

tot=maths+eng+kisw+science+sst
print(tot)
avg=tot/5
print(avg)

if avg>=80 and avg<=100:
    print("A")
elif avg>=75 and avg<=79:
    print("A-")
elif avg>=70 and avg<=74:
    print("B+")
elif avg>=65 and avg<=64:
    print("B")
elif avg>=60 and avg<=69:
    print("B-")
elif avg>=55 and avg<=59:
    print("C+")
elif avg>=50 and avg<=54:
    print("C")
elif avg>=45 and avg<=49:
    print("C-")
elif avg>= 40 and avg<=44:
    print("D+")
elif avg>=35 and avg<=39:
    print("D")
elif avg>=30 and avg<=34:
    print("D-")
elif avg >=0 and avg <=29:
    print("E")
else:
    print("Invalid")





