# Use cwd an sys to import Reter
import sys
sys.path.append("../../")
from reter.reter import (
    init,
    indicator,
    captureKey
)


#-- Issues being tested
#~~ #5, #6

#-- Issues found
#~~ setPos

#-- Fixed issues
#~~ #5, #6, setPos
'''
terminal = init()
initPos = terminal.cursor.getPos()
print("tester lester")
chunks = terminal.line.chunkIt(terminal.screen, " ", 1)
chunks[0].setColour(terminal.cursor, indicator.colour.fg.blue)
terminal.cursor.setPos(initPos[0], initPos[1])
while True:  # Just keep script running
    pass
'''
