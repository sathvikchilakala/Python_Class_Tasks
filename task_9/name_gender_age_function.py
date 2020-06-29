def f1(name,age,gender,) :

    if gender not in ["male", "female"]:
        print("Enter female or male for gender.")
        return None
    if not age.isdigit():
        print("Enter numbers for your age.")
        return None
    print('Hello', name, ',you are', gender, 'and are', age, 'years old!')

name = input('Enter your name (letters): ')
age=input('Enter your age (number): ')
gender=input('Enter your gender (male/female): ')
f1(name, age, gender)

