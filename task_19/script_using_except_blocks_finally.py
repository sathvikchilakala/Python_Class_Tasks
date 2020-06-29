try:
    first_name, last_name = str(input("Enter your first and last name separated by a comma(,): "))
    user_input_1 = int(input(("Enter the number you would like to divide: ")))
    user_input_2 = int(input(("Enter the number you would like to divide by: ")))
    age = int(input("Enter your age: "))
    ans = user_input_1/ user_input_2
    full_name = first_name + last_name
    print(full_name)
    print(age)
    print("If you divide", user_input_1, "with", user_input_2, "you get:", ans)

except ZeroDivisionError:
    print("Dividing by 0 will produce an error (It is an undefined number). Pick another number")

except SyntaxError:
    print("You forgot a comma between your first and last name")

except ValueError:
    print("Your age cannot be negative")

except NameError:
    print("Enter your name")

finally:
    print("Thank you, I hope you got your information!!!")
    