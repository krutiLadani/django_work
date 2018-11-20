#use of user define exception
class MyException(Exception):
	def __init__(self,value):
		self.value = value
def  checkValue(num):
	try:
		if num>50:
			raise MyException(num)
	except MyException as me:	
		print "You have to enter number between 0-50 only, you entered :",me.value
num1 =  input("Enter a number between 0-50 :")
checkValue(num1)