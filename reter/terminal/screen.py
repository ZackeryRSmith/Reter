########################################
# IMPORTS
########################################

import re
import sys
import os
from typing import Optional
sys.path.append("../../")  # Go to master
from reter.style.indicator import indicator
from reter.cursor.cursor import Cursor 


########################################
# SCREEN
########################################

class Screen:
    def __init__(self, cursor, height: Optional[int]=None, width: Optional[int]=None, linkCursor: Optional[bool]=False, autoCalibrate: Optional[bool]=True):
        self.terminal = sys.stdout  # Allows us to track printed text
        self.cachedScreen = ""
        self.cursor = cursor
        if autoCalibrate:
            self.height = self.getDimensions(returnFormat="lines") if height == None else height
            self.width = self.getDimensions(returnFormat="columns") if width == None else width
        else:
            self.height = height
            self.width = width
 
        # Does nothing as of now
        if linkCursor:
            # Link cursor to screen
            self.cursor.link()


    # Not implemented.. not too sure if it every will. Reter is not a graphic lib so there is no need for this
    def setBorder(self, theme={"topLeftCorner": "+", "botLeftCorner": "+", "topRightCorner": "+", "botRightCorner": "+", "connections": "-"}):
        """
        """
        pass


    def returnDimensions(self, returnFormat: Optional[str]="WxH"):
        """
        Returns current set dimensions for screen object. To update dimensions or fetch new ones use getDimensions().

        :param str returnFormat: The format in which to be retuned in
        """
        if returnFormat == "WxH":
            return str(self.width)+"x"+str(self.height)


    def getDimensions(self, returnFormat: Optional[str]="WxH", clearScreen: Optional[bool]=True, xory: Optional[str]=None, positiveyLimit: Optional[int]=None, negativeyLimit: Optional[int]=None, positivexLimit: Optional[int]=None, negativexLimit: Optional[int]=None):
        """
        Gets current screen dimensions
        
        :param str returnFormat: The format in which to be retuned in
        :param bool clearScreen: If false screen will not be cleared when checking dimensions. This can cause some weird visual bugs if not expected and dealt with manually!!
        :param string xory: If "x" the returned value just be columns and vice versa. If xory equal to NoneType then (Columns, Lines) will be returned.
        
        :: DEPRECATED
        :param int positiveyLimit: This will set the dimensions limit on positive y direction
        :param int negativeyLimit: This will set the dimensions limit on negative y direction
        :param int positivexLimit: This will set the dimensions limit on positive x direction
        :param int negativexLimit: This will set the dimensions limit on negative x direction
        
        :rtype: Return varies depending on the value of `xory` but by default a tuple will be returned.
        :return: Return varies depending on the value of `xory` but by default (Columns, Lines) will be returned.
        """
        if clearScreen:
            os.system("clear")
        terminal_size = os.get_terminal_size()
        if returnFormat == "WxH":
            return str(terminal_size.columns)+"x"+str(terminal_size.lines)

        elif returnFormat == "HxW":
            return str(terminal_size.lines)+"x"+str(terminal_size.columns)
        
        elif returnFormat == "xy":
            return (terminal_size.columns, terminal_size.lines)
        
        elif returnFormat == "yx":
            return (terminal_size.lines, terminal_size.columns)
        
        elif returnFormat == "x":
            return terminal_size.columns
        
        elif returnFormat == "y":
            return terminal_size.lines
        
        elif returnFormat == None:
            return (terminal_size.lines, terminal_size.columns)
        
        else:
            return posY, negY, posX, negX


    def setDimensions(self, columns, lines):
        pass


    def wipe(self):
        """
        Cleans off screen of all text. Be warned this also cleans the cachedScreen variable, if needed you may save cachedScreen to another
        variable... It's a double cache how fun!!
        """
        self.cachedScreen = ""
        os.system("clear")


# May or may not be moved into a diffrent path at some point
########################################
# LINE
########################################

class Line:
    def __init__(self, cursor):
        self.cursor = cursor
                   

    def returnLineNumber(self):
        """
        Gets current line number
        
        :rtype: int
        :return: Returns current line number cursor sits on
        """
        return self.cursor.getPos("y")


    def chunkIt(self, screen, pattern, lineNumber, maxChunk: Optional[int]=None):
        """
        The chunkIt function will split by a pattern (kinda like str.split()), it will store these chunks as Chunk(). The chunk object can
        be moved, and minuplated to how you like. For more clarification here is an example. Lets say we have some text printed on the
        terminal I.e. "The quick brown fox" we can take this and chuck by whitespace by using chunkIt like so, chunkIt(1, " ") would return
        4 chunk objects I.e. "The", "quick", "brown", and "fox". These can then be manupulated (Anything from colour to deletion)! 

        WARNING:: chunkIt uses the cachedScreen variable to get it's data! cachedScreen is not perfect and requires the end-user to maintain a
        stable code structure!! Look at the wiki for best practices and how to get back on track if you *MUST* get off track to do something.
        I hope the logging system will be more stable at a later date but for now this is how it must be.

        NOTE:: Any chunk manupulated will be placed back in the same place on the same line, this is unless the end-user decides to change 
        said position!

        :param int lineNumber: Line in which to chunk. By default it will chunk where the cursor is located
        """
        if lineNumber == None:
            lineNumber = self.returnLineNumber()
        try:
            rawValue = screen.cachedScreen.split("\n")[lineNumber-1]
        except AttributeError:
            # Fix this error to use custom error handler (/errhandler/)
            sys.exit(indicator.colour.formatting.bold+indicator.colour.formatting.underline+"Hey it seems you did not pass a screen object... You have passed a '%s' object" % (type(screen)))

        # Check for regex
        try:
            # Do some manual checks for re
            if pattern.isspace():
                raise re.error("Intentionaly raised error")
            isRe = re.compile(pattern)
        except re.error:
            isRe = False
        if isRe:
            # Deal with regular expression here
            pass
        else:
            # Uses "".split() to split string (Taking the easy way out.. this code is subject to change!)
            splitValue = (rawValue.split(pattern) if maxChunk == None else rawValue.split(pattern, maxChunk))
            # Remove random items and whitspace from splitValue
            removeSpace = [x.strip(' ') for x in splitValue]
            removeRandom = [x for x in removeSpace if not x.startswith('\x1b')]
            deleteEmpty = [item for item in removeRandom if item.strip()]
            splitValue = deleteEmpty
            # Convert list of strings to a list of chunk objects
            for index, item in enumerate(splitValue):
                # Get positions of items on screen
                for match in re.finditer(splitValue[index], rawValue):  # A wee bit of re
                    position = (lineNumber, match.start(), match.end())
                splitValue[index] = Chunk(position, item)
            return splitValue

    def remove(self, lineNumber):
        """
        """
        # Delete entire chunk (Line deletion needs to be implemented first)
        pass


# May or may not be removed or put into another path
########################################
# CHUNK
########################################

class Chunk:
    """DOCSTRING NOT CREATED YET!"""
    def __init__(self, position, value):
        self.position = position
        self.value = value
        self.formatting = {}


    def setColour(self, cursor, fg: Optional[str]=None, bg: Optional[str]=None):
        """
        Sets an entire chunks colour. FG and BG are supported.. additional slots may be added in the future!

        :param object cursor: Cusor object, with a terminal object you can just pass `terminal.cursor`
        :param str fg: Foreground colour
        :param str bg: Background colour
        """
        initPos = cursor.getPos()
        stripped = self.value.rstrip()
        cursor.setPos(self.position[1]+1, self.position[0]) 
        # stdout.write() issue. https://github.com/ZackeryRSmith/Reter/issues/2
        #sys.stdout.write(("" if fg == None else fg)+("" if bg == None else bg)+stripped+indicator.colour.formatting.eoc)
        print(("" if fg == None else fg)+("" if bg == None else bg)+stripped+indicator.colour.formatting.eoc)
        cursor.setPos(initPos[0], initPos[1])
        self.formatting.update({
            "colour": {
                "fg":fg,
                "bg":bg
            }
        })


    def setPos(self):
        """
        """
        pass


    def move(self, cursor, x, y):
        """
        Moves a chunk
        """
        # This should be re-worked. There were quite of weird bugs that should not be overlooked although patched.

        # Move cursor to ending chunk position
        cursor.setPos(self.position[2]+1, self.position[0])
        # Delete chunk
        for i in range(self.position[1], self.position[2]):
            sys.__stdout__.write("\b")
            sys.__stdout__.write(" ")
            sys.__stdout__.write("\b")
        # Move cursor to starting chunk position
        cursor.setPos(self.position[1]+1, self.position[0])
        # Move cursor to desired position
        print(" " if x > 1 else "", end="")  # If x is bigger then 1 some weird things happen. This fixes it
        cursor.move(x-1, y) if self.position[1] == 0 else cursor.move(x, y)  # Turnary operator fixes some formatting bugs
        # Place chunk
        print(("" if self.formatting["colour"]["fg"] == None else self.formatting["colour"]["fg"])+("" if self.formatting["colour"]["bg"] == None else self.formatting["colour"]["bg"])+self.value.rstrip()+indicator.colour.formatting.eoc)
        # Update self.position
        self.position = (self.position[0]+y, self.position[1]+x, self.position[2]+x)


    def returnValue(self):
        """
        Returns value stored in chunk
        """
        return self.value
    

    def returnPosition(self):
        """
        Returns position of value stored in chunk
        
        :rtype: tuple of int's
        :return: Returns (starting_char_position, ending_char_position, line_number)
        """
        return self.position


