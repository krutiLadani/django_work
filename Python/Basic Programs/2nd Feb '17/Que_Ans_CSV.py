#program for creating CSV file and store questions and answers
import csv
#this is the dictionary with keys/questions only
questions = {"OS computer abbreviation usually means ?":"",
			".MOV extension refers usually to what kind of file?":"",
			"Who developed Yahoo?":"",
			"DB computer abbreviation usually means ?":"",
			".JPG extension refers usually to what kind of file?":""}
print "\n****** Let's check your General Knowledge ******"
queNo = 1
for que in questions:
	print str(queNo)+". "+que
	queNo+=1
	ans = raw_input("Enter Answer :")
	questions[que]=ans #adding the answers to dictionary value 

with open('GKTest.csv', 'w') as csvfile:
    fieldnames = ['Questions', 'Answers']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for key in questions.iterkeys():
	    writer.writerow({'Questions': key, 'Answers': questions[key]})
queNo=1
print "***** Here is your answers *****"
with open('GKTest.csv') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         print "Questions",queNo,":",row['Questions']
         print "Answer :",row['Answers']
         queNo+=1