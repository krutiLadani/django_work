#use of  **kwargs 
def starStarKwArgs(**data):
	if data is not None:
		for key, value in data.iteritems():
			print "{0} = {1}".format(key,value)
starStarKwArgs(name="Bhumik",surname="Dhrangadhriya",
				age="21",bloodgroup="B+",work="DRC Systems")