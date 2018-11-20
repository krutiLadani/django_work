class Parent:

	def add(self,a,b):
		return a+b

class Child(Parent):

	def add(self,a,b):
		return a*b

obj = Child()
print obj.add(5,5)