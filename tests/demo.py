from reter import captureKey, indicator
import os

varList = ["Hello", "World", "Peekaboo", "Rain", "Sleet"]
varValues = [15, 0, -18.3, 10, 2]
varIndex = 0

def updateInfo():
    global varList
    global varValues
    global varIndex
    if varIndex > len(varList)-1:
        varIndex -= len(varList)
    elif varIndex < 0:
        varIndex += len(varList)
    os.system("clear")
    print("""
          %s
          %s

            %s
""" % (varList[varIndex], varValues[varIndex], varIndex+1))

while True:
    key = captureKey()
    if key==indicator.arrow.up:
        varValues[varIndex] += 1

    elif key==indicator.arrow.down:
        varValues[varIndex] -= 1
    
    elif key==indicator.arrow.right:
        varIndex += 1
    
    elif key==indicator.arrow.left:
        varIndex -= 1
    
    updateInfo()
