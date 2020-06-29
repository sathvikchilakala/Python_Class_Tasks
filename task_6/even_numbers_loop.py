even_numbers=[]
number=50
while number<=100:
    even_numbers.append(number)
    number = number + 2
print("The even numbers from 50 to 100 are:", str(even_numbers).strip('[]'))