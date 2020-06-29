class A:
    def i(self):
        print("Class 1")


class B(A):
    def i(self):
        print("Class 2")


class C(A):
    def i(self):
        print("Class 3")

obj = C()
obj.i()

B.i(obj)
C.i(obj)
A.i(obj)