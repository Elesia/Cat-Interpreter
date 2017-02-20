def userForLoop(lst,tabCount):
    rangeBegin = lst[2]
    rangeEnd  = lst[4]
    iterator = lst[1]

    printedCommand = tabCount+"for "+ iterator + " in range(" + rangeBegin + ", " + rangeEnd + "):\n"
    return printedCommand

def saveFile(filename,content):
    commandText = open(filename, "a")
    commandText.write(content)
    commandText.close()
