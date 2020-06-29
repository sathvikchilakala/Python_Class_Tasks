list_1 = [9, 13, 8, 37, 294, 13, 65838]
print("Maximum value:", max(list_1))
print("Minimum value:", min(list_1))
print("Length:", len(list_1))
print("Sum:", sum(list_1))
list_1.insert(4, 11)
print("After inserting 11 into the 4th position:", list_1)
list_1.remove(37)
print("After removing the 37 from the list:", list_1)
list_1.append(2344)
print("After adding 2344 to the end of the list:", list_1)
list_1.reverse()
print("After reversing the order of the list it is:", list_1)
list_1.pop(6)
print("After removing the last number in the list (9):", list_1)
remove = list_1.pop(2)
print("The pop with index command will remove the number of the index chosen:", remove)
list_1.count(0)
print("The count function shows that 13 appears twice in the list, so it deletes one of them:", list_1)
list_1.sort()
print("The sort command shows the list in ascending order:", list_1)
index = list_1.index(294)
print("The number 294 shows up in the list at:", index)
enum = enumerate(list_1)
print("The enumerate function shows the index of each of the intgers in the list:", list(enumerate(list_1)))
del(list_1[3])
print("The delete operator works like the remove function:", list_1)
list_2 = [47, 29, 5, 238]
list_1.extend(list_2)
print("The extend function adds whatever you numbers you have chosen to the given list", list_1)
list_3 = [12, 68, 111, 378, 468]
list_2= list_2 + list_3
print("List concatenation can be done with addition signs:", list_2)
list_4 = []
for l in list_1:
    list_4.append(l**2)
print("List comprehension can be done with the append command, this will list its squares", list_4)

while list_1==list_1:
    print("This is an infinite loop because they will always be equal")



