print("\n-----------------------------------")
print("\nAll the conditions in python :")

print("\n#1 IF STATEMENT")

varNum1 = input("Enter No 1 :")
varNum2 = input("Enter No 2 :")

if varNum1>varNum2:
	print("%d is greater than %d" %(varNum1,varNum2))

print("\n#2 IF..ELSE STATEMENT")

varNum1 = input("Enter No 1 :")
varNum2 = input("Enter No 2 :")

if varNum1>varNum2:
	print("%d is greater than %d" %(varNum1,varNum2))
else:
	print("%d is greater than %d" %(varNum2,varNum1))

print("\n#3 ELSE IF(elif) STATEMENT")

varNum1 = input("Enter 10/20/30 :")

if varNum1==10:
	print("Number is 10")
elif varNum1==20:
	print("Number is 20")
elif varNum1==30:
	print("Number is 30")
else:
	print("Wrong Number")


print("\n#4 NESTED IF STATEMENT")

varAge = input("Enter your age :")

if varAge>21:
	varMrg = raw_input("Are you married ? (y/n) :")
	if varMrg=='y':
		varChild = input("How many children you have ? :")
		if varChild < 2:
			print("Okay that's fine !")
		else:
			print("No Comments !")
	else:
		varStud = raw_input("Are you Student ? (y/n) :")
		if varStud=='y':
			print("Okay that's fine !")
else:
	print("Enjoy !")

print("\n-----------------------------------\n")