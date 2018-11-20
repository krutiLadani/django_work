#use of lambda
def doubleNumber(num):
	return lambda x : x * num
num1 = input("Enter Any Number to make Double of it :")
doubleNum = doubleNumber(num1)
print "Double of your number is :",doubleNum(2)