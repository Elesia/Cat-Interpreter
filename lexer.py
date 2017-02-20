import sys
import lexerFunctions as lexfun
# print sys.argv[1]

tabIndent=""
lineNumber=0
outFile=open(sys.argv[1]+'PyCode.py', 'w')


with open (sys.argv[1], 'r') as inFile:
	for line in inFile:
		lineNumber+=1
		lineTokens=line.split()
		if lineTokens[0]=="loop":
			tabIndent=lexfun.kickLoop(lineTokens, lineNumber, outFile, tabIndent)
			
		elif lineTokens[0]=="endloop":
			tabIndent=tabIndent[0:-4]

		else:
			outFile.write(tabIndent + ' '.join(lineTokens) + '\n')
			
