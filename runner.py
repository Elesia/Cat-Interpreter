import functions as f

def main():
    commandList = []
    userInput = open("commandInput.txt","r")
    tabCount = ""
    for aline in userInput:
        lineTerminate = False
        while not lineTerminate:
            commandList = aline.split()
            print commandList
            if commandList:
                if (commandList[0].lower() == "loop"):
                    printer = f.userForLoop(commandList,tabCount)
                    tabCount +="    "
                    f.saveFile("commandOutput.py",printer)
                elif (commandList[0] == "end"):
                    tabCount=tabCount[0:-4]
                    
                lineTerminate = True
            else:
                break

main()
