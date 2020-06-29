user_number = int(input(" Enter your number : "))
odd_sum = 0

for i in range(1, user_number + 1):
    if (i % 2 == 0):
        print("This is an even number, enter an odd number.")
    else:
        odd_sum = odd_sum + i
    print("The Sum of Odd Numbers from 1 to {0} = {1}".format(i, odd_sum))




'''
user_number = int(input("Enter your number: "))
x = 1
for i in range(1, user_number):
    thenumber = x+1
    print(thenumber, "and", user_number)






odd_numbers=[]
number=1
while number<100000:
    odd_numbers.append(number)
    number = number + 2
print("The odd numbers from 1 to 100 are:", str(odd_numbers).strip('[]'))
if (user_number % 2) == 0:
    print(user_number, "is  an even number. Enter an odd number.")
elif user_number//2 > 1:
print("The sum of the odd numbers it takes for", user_number, "to get to 1 is", number)
'''
