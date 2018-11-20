import csv
queNo=1
QueAns = {}
print "****** Let's check your Computer GK******\n"
with open("questions.csv") as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print queNo,".",row['Questions']
		queNo+=1
		ans = raw_input("Enter Answer :")
		QueAns[row['Questions']] = ans

with open('questions_answers.csv', 'w') as csvfile:
    fieldnames = ['Questions', 'Answers']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for key in QueAns.iterkeys():
	    writer.writerow({'Questions': key, 'Answers': QueAns[key]})