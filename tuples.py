#tuples are immutable
days=("Mon","Tue","Wed","Thur","Fri","Sat","Sun")
print(days)

#days.append("myday")

numbers=[1,2,3,4,5,6,7,8]
print(numbers)
numbers[2]=11
print(numbers)

print(days[3])

#days[3]="March"
print(days)

userName="Mark Zuckeburg"
password="pwd"

myDbValues=(1,"Mark Zuckeburg","password",38,"male",["values"])

myDbValues[5].append("key")
myDbValues[5].append ({"MOTHER":"TERESA"})
print(myDbValues)
#myDbValues[0]=12
#print(myDbValues)
un=myDbValues[1]
print(un)

pss=myDbValues[2]
print(pss)

# ==strict equality operator
# = put a value inside a variable
if un==userName:
    print("username true")
else:
    print("username false")

if pss == password:
    print("password true")
else:
    print("password false")

#Dictionaries
#Is a data structure that stores data as key value pairs

myDictionary={"username":"Mark Zuckerburg","password":"pwd","age":38 ,"gender":"male"}
print(myDictionary["username"])
print(myDictionary["password"])
print(myDictionary["gender"])

mySelf={"firstname":"Kui",
        "lastname":"Munyua",
        "schools":
            {"primary":[{
                "schoolName":"kilimani",
                "population":500,
                "headteacher":"Fridah"

            },
                {"primary":"milimani",
                "population":600,
                 "headteacher":"Keren"}

            ]
             }
}

# print(mySelf["schools"]["primary"][])