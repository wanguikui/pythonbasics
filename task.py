
taskList=[23,"Jane",["lesson 23",560,{"currency":"KES"}],987,(76,"John")]

print(type(taskList))

print(taskList[2][2]["currency"])
#d=taskList[2][2]
#print(d)



print(taskList[2][1])

print(len(taskList))

# 987 to 789
taskList[3]=789
print(taskList)


#taskList[4].append("Jane")



ls1=[123,34,54645,34,5]
ls1.sort()
print("Largest element is:",ls1[-1])

profit={
    "cost_price":32.67,
    "sell_price":45.00,
    "inventory":1200
}
