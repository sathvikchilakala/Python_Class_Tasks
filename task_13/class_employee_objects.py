class Employee:
    eno = 4257963638
    ename = 'Johnathan Jordan'
    esalary = 56000

    def display(self):
        print("Employee Details")
        print("-"*50)
        print("The employee's number is", self.eno)
        print("The employee's name is", self.ename)
        print("The employee's salary is", self.esalary)
        print("This employee will join")


employee1 = Employee()
print("Accessing the variables individually")
print(employee1.eno)
print(employee1.ename)
print(employee1.esalary)
print("Complete data of the student1")
employee1.display()
