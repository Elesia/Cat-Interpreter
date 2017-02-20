def kickLoop(lineTokens, lineNumber, outFile, tabIndent):
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

	return tabIndent


