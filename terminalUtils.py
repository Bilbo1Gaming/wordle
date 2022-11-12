from time import sleep
import os

# Clear Function
def clear(): os.system('cls||clear')

# Draw to screen
def draw(data):
    clear()
    for y in range(0,len(data)):
        xBuffer = ""
        for x in range(0,len(data[y])):
            xBuffer = xBuffer + data[y][x]
        print(xBuffer)
    

def box(boxX,boxY):
    yArray = []
    for y in range(boxY):
        if y in range(1,boxY-1): yArray.append(buildDrawArray("|"," ",boxX))
        else: yArray.append(buildDrawArray("|","-",boxX))
    return(yArray)

def buildDrawArray(endBlocks,midBlocks,size):
    builtArray = []
    for i in range(size):
        if i in range(1,size-1): builtArray.append(midBlocks) 
        else: builtArray.append(endBlocks)
    return(builtArray)

def addText(box, row, text):
    testArray = [[1,2,3],[4,5,6]]
    testArray[1][1] = 7
    for i in range(len(testArray)):
        for j in range(len(testArray[i])):
            print(testArray[i][j])

# draw(box(width,height)

# text(box, row, text)
