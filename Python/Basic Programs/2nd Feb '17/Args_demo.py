#use of  *args 
def starArgs(hobby,*hobbies):
    print "Your hobby is :",hobby
    for arg in hobbies:
        print "Your another hobby is : ",arg

starArgs("Cricket","Vollyball","FootBall","Listen Music")