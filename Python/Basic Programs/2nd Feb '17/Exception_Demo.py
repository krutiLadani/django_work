#Use of Exception 
def divisionFunc(num1,num2):
	try:
		print num1/num2;
	except ZeroDivisionError:
		print "---You can not divide any no with zero---"
num1 = input("Enter Any Number :")
num2 = input("Enter Another Number :")
divisionFunc(num1,num2)