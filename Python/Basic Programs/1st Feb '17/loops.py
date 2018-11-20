print("\n-----------------------------------")
print("\nAll the Loops in python :")

print("\n#1 For Loop")

varNum = input("Enter any Number :")

for varNum in range(varNum+1):
	print(varNum)
else: 
	print("This is Default Else !!")
print("\n#2 While Loop")

varTemp = 'y'

while (varTemp=='y'):
	print("""\tYou are in Loop
\tpress y to be in the loop  OR
\tpress any key to leave """)
	varTemp = raw_input();

print("\n-----------------------------------\n")