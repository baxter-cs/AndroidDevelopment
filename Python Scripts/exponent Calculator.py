print "Try 15"
base = raw_input("input base number?")
exponent = raw_input("input exponent?")
def runloop(resultn):
	resultx = str(resultn)
	for letter in resultx:     # First Example
		print 'Current Number :', letter
	print "The Number you Printed off is: " + resultx
def convertStr(s):
    """Convert string to either int or float."""
    try:
        ret = int(s)
    except ValueError:
        #Try float.
        ret = float(s)
    return ret
def checkNumSize(x):
	if x > 15**150000:
		print "values may be too large to print."
		print "Press CTRL + c if nothing loads after 20 seconds"

basex = convertStr(base)
exponentx = convertStr(exponent)
checkNumSize(basex**exponentx)
runloop(basex**exponentx)
