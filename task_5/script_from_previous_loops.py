name = str(input("Enter your phrase to calculate the number of vowels and consonants:"))
con=0
vow=0
num=0
sym=0
spc=0
for a in name:
    if a not in "aeiouAEIOU" and a not in "1234567890" and a not in "!@#$%^&*()<>?:,./;'[]\=-" and a not in " ":
        con=con+1
    elif a in "1234567890":
        num=num+1
    elif a in "!@#$%^&*()<>?:,./;'[]\={}|-":
        sym=sym+1
    elif a in "aeiouAEIOU":
        vow=vow+1
    elif a in " ":
        spc=spc+1
print("The total number of vowels in", name, "is:", vow, "!")
print("The total number of consonants in", name, "is:", con, "!")
print("The total number of numbers in", name, "is:", num, "!")
print("The total number of symbols in", name, "is:", sym, "!")
print("The total number of spaces in", name, "is:", spc, "!")