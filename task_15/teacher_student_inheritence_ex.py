class teacher:
	def setid(self,id):
		self.id = id
	def getid(self):
		return self.id
	def setname(self,name):
		self.name = name
	def getname(self):
		return self.name
	def setsalary(self,sal):
		self.sal = sal
	def getsalary(self):
		return self.sal

class student(teacher):
	def setmarks(self,marks):
		self.marks = marks
	def getmarks(self):
		return self.marks
s = student()
s.setid(1001)
s.setname('PAVAN')
s.setmarks(98)

print("student id is:",s.getid())
print("student name is ",s.getname())
print("student marks is",s.getmarks())
