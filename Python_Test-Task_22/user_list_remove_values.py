my_list = [14, 68, 47, 57, 3, 79, 93, 11]
print("This list contains numbers from 1 through 100!")
x = int(input("Enter a number that you think will be in my list: "))
if x in my_list:
    print("The number", x, "is in my list!!!")
    my_list.remove(x)
    print(my_list)
else:
    print("The number", x, "is not in the list. The list's numbers were:", my_list)


