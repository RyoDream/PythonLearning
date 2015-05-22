a=3
def firstSampleFunc():
	print a


b=3
def secondSampleFunc():
	print b     # got SyntaxWarning: name 'b' is used prior to global declaration
	global b
	b=4
	print b


c=3
def thirdSampleFunc():
	print c
	c = 4       # got UnboundLocalError: local variable 'c' referenced before assignment
	print c

firstSampleFunc()
secondSampleFunc()
thirdSampleFunc()

