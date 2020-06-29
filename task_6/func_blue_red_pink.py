def blue ():
    print("You like the color blue !")
def red ():
    print("You like the color red !")
def pink ():
    print("You like the color pink !")
col=input("What color do you like?: ")
if col=="blue":
    blue()
elif col=="red":
    red()
elif col=="pink":
    pink()
else:
    print("Not a valid color.")
