def  add(a,b) :
    "It returns sum of a,b"
    c=a+b
    print (c)
def  sub(a,b) :
    "It return difference of a,b"
    c=a-b
    print(c)
def  prod(a,b) :
    "It returns product of a,b"
    c=a*b
    print (c)
def  div(a,b) :
    "It returns division of a,b"
    c=a/b
    print(c)
def sqr(a) :
    "It returns sqt returns square of a"
    c=a*a
    print (c)
def cube(a) :
    "It returns cube of a"
    c=a*a*a
    print(c)
def power(a,b) :
    "It returns power of a to the b"
    i=1
    c=a #2
    if b==0 :
        print(1)
    else :
        while i<b :
            c=c*a
            i=i+1
        else :
            print (c)
while True :
    print("Main Menu")
    print("---------")
    print("1. Add")
    print("2. Sub")
    print("3. Product")
    print("4. Division")
    print ("5. Square")
    print ("6. Cube")
    print ("7.Power")
    print ("8. Quit")


    ans=int(input("Enter choice[1-8] : ")) #18
    if ans==1 :
        x=int(input("Enter number1 : "))
        y=int(input("Enter number2 : "))
        add(x,y)
    elif ans==2 :
        x=int(input("Enter number1 : "))
        y=int(input("Enter number2 : "))
        sub(x,y)
    elif ans==3 :
        x=int(input("Enter number1 : "))
        y=int(input("Enter number2 : "))
        prod(x,y)
    elif ans==4 :
        x=int(input("Enter number1 : "))
        y=int(input("Enter number2 : "))
        div(x,y)
    elif ans==5 :
        x=int(input("Enter number : "))
        sqr(x)
    elif ans==6 :
        x=int(input("Enter number : "))
        cube(x)
    elif ans==7 :
        x=int(input("Enter number1 : "))
        y=int(input("Enter number2 : "))
        power(x,y)
    elif ans==8 :
        print("Thank you.")
        break
    else :
        print("Wrong choice.Try again")
