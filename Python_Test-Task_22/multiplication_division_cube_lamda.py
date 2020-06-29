multi = lambda x, y, z: x * y * z
x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
z = int(input("Enter a number: "))

def multi_func(x, y, z):
    return x * y * z

print("After using the lambda function to multiply", x, ",", y, "," + "and", z, "the answer is", (multi_func(x, y, z)))


div = lambda a, b, c: a / b / c
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

def multi_func(a, b, c):
    return a / b / c

print("After using the lambda function to multiply", a, ",", b, "," + "and", c, "the answer is", (multi_func(a, b, c)))


def cube(i):
    return i*i*i
my_list = [1,2,3,4,5,6,7,8,9,10]
cubes = map(cube, my_list)
ans = map(str, cubes)
print(','.join(ans))
