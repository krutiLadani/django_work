#file handling
file = open("testfile.py","w") #creating the python file testfile.py
file.write("def addNum(num1,num2): \n")
file.write("	return  num1+num2")
file.close()

file = open("testfile.py","a")#appending another function to testfile.py
file.write("\ndef mulNum(num1,num2): \n")
file.write("	return num1*num2")
file.close()

import testfile #import that file
num1 = input("Enter A Number :")
num2 = input("Enter Another Number :")
print "Addition is :",testfile.addNum(num1,num2)
print "Multiplication is : ",testfile.mulNum(num1,num2)

print "The code is :"
with open("testfil.py","r") as file: #open that file to read using WITH
	code = file.read()
	print code
file.close()