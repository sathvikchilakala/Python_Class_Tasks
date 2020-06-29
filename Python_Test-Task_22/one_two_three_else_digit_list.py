one_list = []
two_list = []
three_list = []
four_list = []
while True:
    x = str(input("Enter a 1 digit, 2 digit, 3 digit, or any number: "))
    if x.isdigit():
        z = int(x)
        w = int(x)
        y = 0
        while w > 0:
            w = w // 10
            y = y + 1
        if y == 1:
            one_list.append(z)
        elif y == 2:
            two_list.append(z)
        elif y == 3:
            three_list.append(z)
        else:
            four_list.append(z)
        print("List with one digits:", one_list)
        print("List with two digits:", two_list)
        print("List with three digits:", three_list)
        print("List with four plus digits:", four_list)
        a = str(input("Would you like to put in another number? Answer either yes/no: "))
        if a == 'yes':
            continue
        else:
            print("Thank you for using the program!")
            break
    else:
        print(x, "is not a valid number. Enter a real number.")
