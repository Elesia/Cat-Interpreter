import sys
# print sys.argv[1]

tabIndent=""

outFile=open('tempCode.py', 'w')

with open (sys.argv[1], 'r') as inFile:
	for line in inFile:
		x=0
		lineTokens=line.split()
		if lineTokens[0]=="loop":
			if lineTokens[1]:
				loopVariable=lineTokens[1]
			if lineTokens[2] and lineTokens[2]!="from":
				break
			if lineTokens[3]:
				loopFrom=lineTokens[3]
			if lineTokens[4] and lineTokens[4]!="to":
				break
			if lineTokens[5]:
				loopTo=lineTokens[5]
			if lineTokens[6] and lineTokens[6]!="jump":
				break
			if lineTokens[7]:
				loopJump=lineTokens[7]

			outFile.write(tabIndent + 'for ' + loopVariable + ' in range(' + loopFrom + ' ,' + loopTo + ', ' + loopJump + ') :\n')

			tabIndent+="	"

		elif lineTokens[0]=="endloop":
			tabIndent=tabIndent[0:-4]

		else:
			outFile.write(tabIndent + ' '.join(lineTokens) + '\n')
			
