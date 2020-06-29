'''
def strlen(x) : #harika
    cnt=0
    for i in x :
        cnt=cnt+1
    print("Length of ",x," is : ",cnt)

def  str_vowels_cnt(x) :
    cnt=0
    for i in x :
        if i in "aeiouAEIOU" :
            cnt=cnt+1
    print("Total no of vowels in ",x ,"is : ",cnt)

x=input("Enter a string :")
strlen(x)
str_vowels_cnt(x)
'''
