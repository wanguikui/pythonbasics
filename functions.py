#we use def for function declaration. after the key word def you write the name of the function the
#inside the ()the xy is called a parameter. you can have any number of parameters
#on the evenOdd function number and string are arguments. input you give to a function. the input we give is copied to
# our parameters
def evenOdd(xy,tn):

    if xy%2==0:
        print("even")
    else:
        print("odd")
        print(tn)

evenOdd(9,"thanks")

#def sum(a,b,c,d):
    #total=a+b+c+d
    #print(total)

#sum(1,2,3,4)

def test(name="Jane Doe"):
    print("{}".format(name))

test("Mary Jane")

#string concatination
#print("mangoes"+" "+"eggs")

#string formatting
#name=input("What is your name ")
#fruit=input("What's your fav fruit ")
#fstring
#print(f"My name is: {name}")
#print(f"My fav fruit is: {fruit}")
#value=fruit
#print("My name is: {}".format(name))
#print("My fav fruit is: {}".format(fruit))
#print("My fav {} is: {}".format(valuefruit))

#ARGS * unlimited positional arguments
#**kwargs research

def summ(*args):
    print(args)
    #print(sum(args))

    total=0
    for each in args:
        #total+=each
        total=total+each

    print(total)


summ(10,40,80,10)
summ(10,40,10)
summ(10,40,50,10)
summ(10,40,30,10)






