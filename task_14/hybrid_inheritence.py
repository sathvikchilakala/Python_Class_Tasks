class child(  object  ):
    def __init__(self,name,number):
        self.name = name
        self.number = number
    def show(self):
        print(self.name)
        print(self.number)
class student(  child  ):
    def __init__(self,name,number):
        child.__init__(self, name, number)

x = student("Johnathan Goring", 189765)
x.show()
