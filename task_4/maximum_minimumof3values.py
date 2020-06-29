number_1=int(input("Enter your first number: "))
number_2=int(input("Enter your second number: "))
number_3=int(input("Enter your third number: "))
if number_1>=number_2 and number_1>=number_3:
    print(number_1, "is the greatest value!")
elif number_2>=number_1 and number_2>=number_3:
    print(number_2, "is the greatest value!")
elif number_3>=number_1 and number_3>=number_2:
    print(number_3, "is the greatest value!")
if number_1<=number_2 and number_1<=number_3:
    print(number_1, "is the smallest value!")
elif number_2<=number_1 and number_2<=number_3:
    print(number_2, "is the smallest value!")
elif number_3<=number_1 and number_3<=number_2:
    print(number_3, "is the smallest value!")
print("Done!")

"""
if number_1>number_2:
    min=number_2
    max=number_1
else:
    min=number_1
    max=number_2

if max > number_3:
    print("max = " + str(max))
else:
    print("max = " + str(number_3))

if min < number_3:
    print("min = " + str(min))
else:
    print("min = " + str(number_3))
"""