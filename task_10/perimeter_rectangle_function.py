def rectangle(width,length):
   return 2 * (width + length)
width = float(input("Enter the width of your rectangle: "))
length = float(input("Enter the length of your rectangle: "))
perimeter = rectangle(width,length)
print("The perimeter of a rectangle with the width", width, "and the length", length, "is", perimeter)

