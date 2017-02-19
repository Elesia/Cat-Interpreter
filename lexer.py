import sys
# print sys.argv[1]

tabIndent=""
lineNumber=0
outFile=open(sys.argv[1]+'PyCode.py', 'w')

def kickLoop(lineTokens, lineNumber):
	global tabIndent
	try:
		loopVariable=lineTokens[1]
	except:
		print "Error in line " + str(lineNumber)

	try:
		temp=lineTokens[2]!="from"
	except:
		print "Error in line " + str(lineNumber)


	try:
		loopFrom=lineTokens[3]
	except:
		print "Error in line " + str(lineNumber)


	try:
		temp=lineTokens[4]!="to"
	except:
		print "Error in line " + str(lineNumber)


	try:
		loopTo=lineTokens[5]
	except:
		print "Error in line " + str(lineNumber)


	try:
		temp=lineTokens[6]!="jump"
	except:
		print "Error in line " + str(lineNumber)


	try:
		loopJump=lineTokens[7]
	except:
		print "Error in line " + str(lineNumber)


	outFile.write(tabIndent + 'for ' + loopVariable + ' in range(' + loopFrom + ' ,' + loopTo + ', ' + loopJump + ') :\n')

	tabIndent+="	"


	

with open (sys.argv[1], 'r') as inFile:
	for line in inFile:
		lineNumber+=1
		lineTokens=line.split()
		if lineTokens[0]=="loop":
			kickLoop(lineTokens, lineNumber)
			
		elif lineTokens[0]=="endloop":
			tabIndent=tabIndent[0:-4]

		else:
			outFile.write(tabIndent + ' '.join(lineTokens) + '\n')
			
