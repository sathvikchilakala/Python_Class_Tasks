class A:
    def gr(self):
        print("Grandparent- Student")

class B(A):
    def a1(self):
        print("Adults- Test")

class C(A):
    def a2(self):
        print("Adults- Sports")

class D(C,B):
    def ch(self):
        print("Children- Result")


cA = A()
cA.gr()
cB = B()
cB.a1()
cC = C()
cC.a2()
cD = D()
cD.ch()




