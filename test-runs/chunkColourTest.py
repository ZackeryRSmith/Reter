import sys
sys.path.append('../')
from reter.reter import (
    start,
    indicator
)

def main():
    terminal = start()
    print("The quick brown fox")
    print("Cool beans")
    lineOne = terminal.line.chunkIt(screen=terminal.screen, pattern=" ", lineNumber=1)
    lineOne[0].setColour(cursor=terminal.cursor, bg=indicator.colour.formatting.reverse)
    lineOne[1].setColour(cursor=terminal.cursor, fg=indicator.colour.fg.lightblue, bg=indicator.colour.formatting.reverse)
    lineOne[2].setColour(cursor=terminal.cursor, fg=indicator.colour.fg.magenta)
    lineOne[3].setColour(cursor=terminal.cursor, bg=indicator.colour.bg.red)
    lineTwo = terminal.line.chunkIt(screen=terminal.screen, pattern=" ", lineNumber=2)
    lineTwo[0].setColour(cursor=terminal.cursor, bg=indicator.colour.bg.lightyellow)
    lineTwo[1].setColour(cursor=terminal.cursor, fg=indicator.colour.formatting.underline, bg=indicator.colour.formatting.reverse)


if __name__=='__main__':
    main()

