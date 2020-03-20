def even_odd (x):
    if x%2==0:
        return "even"
    else:
        return "odd"


num=int(input("Input your number"))

print(even_odd(num))



def hello(name="Wangui Munyua"):
    print(name)
hello("Hello " "Wangui Munyua")

#area of triangle
def area_of_traingle(base,height):
    return (base*height)/2
base=int(input("enter base"))
height=int(input("enter height"))

print (area_of_traingle(height,base))


#max range
def max_range (base,height):
    return (base+height)-1
base = int(input("value of base"))
height = int(input("value of height"))
print(max_range(height,base))


#first value in a list
def get_first_value(a,b,c):
   return ([a,b,c])
a = int(input("num 1 "))
b = int(input("num 2 "))
c = int(input("num 3 "))
print(get_first_value(a,b,c,)[0])

#total number of legs
def animal_legs(chicken,cows,pigs):
    return (chicken*2+cows*4+pigs*4)
chicken=int (input("num of chicken "))
cows=int (input("num of cows "))
pigs=int (input("num of pigs "))

print(animal_legs(chicken,cows,pigs))

#find largest number

def compare (num1,num2,num3,num4):
    if num1>num2 and num1>num3 and num1 > num4:
        return num1
    elif num2>num1 and num2>num3 and num2>num4:
        return num2
    elif num3 > num1 and num3 > num2 and num3 > num4:
        return num3
    else:
        return num4


lg=compare(1000,1001,857,1)
print(lg)

#difference between largest and smallest values of integers in a list

numList=[10,15,20,2,10,6]

def difference(numList):
    largest =max(numList)
    smallest =min(numList)
    soln = largest - smallest

    return soln

diff=difference(numList)
print(diff)

#function to concatenate two integer lists

def conc (list1,list2):
    return list1+list2
new_list=conc([1,2,3],[4,5,6])
print(new_list)


#a function that takes two strings as arguments and return either True or False

def compare(string1,string2):
    if len(string1)==len(string2):
        return True
    else: return False
checked_string=compare("abc","def")
print(checked_string)

#a function that converts a dictionary into a list, where each element represents a key-value pair.


#k
manufactureDict={"cost_price":float,"sell_price":float,"inventory":int}
cp=float(input("costPrice "))
sp=float(input("sellPrice "))
stock=int(input("inventory "))

profit=sp*stock - cp*stock

print(profit)






