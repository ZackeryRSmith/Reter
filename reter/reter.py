#!/usr/bin/env python
###########################################################################     
#                                                                         #     
#                          Reter (Retry Terminal)                         #     
#                                      ~ Lets try this again..            #     
#                                                                         #     
#  Copyright (c) 2020, Zackery .R. Smith <zackery.smith82307@gmail.com>.  #     
#                                                                         #     
#  This program is free software: you can redistribute it and/or modify   #     
#  it under the terms of the GNU General Public License as published by   #     
#  the Free Software Foundation, either version 3 of the License, or      #     
#  (at your option) any later version.                                    #     
#                                                                         #     
#  This program is distributed in the hope that it will be useful,        #     
#  but WITHOUT ANY WARRANTY; without even the implied warranty of         #     
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          #     
#  GNU General Public License for more details.                           #     
#                                                                         #     
#  You should have received a copy of the GNU General Public License      #     
#  along with this program. If not, see <http://www.gnu.org/licenses/>.   #     
#                                                                         #     
###########################################################################
                        #  Proudly written in Vim  #
                        #    Zackery .R. Smith     #
                        # github.com/ZackeryRSmith #
                        ############################

__author__ = "Zackery Smith"
__email__ = "zackery.smith82307@gmail.com"
__copyright__ = "Copyright © 2020 Zackery Smith. All rights reserved."
__license__ = "GNU GPL-3.0"
__version_info__ = (0, 0, 1)
__version__ = ".".join(map(str, __version_info__))


########################################
# IMPORTS
########################################

import sys
import tty
import termios
import os
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    Iterator,
    List,
    Match,
    Optional,
    Pattern,
    Sequence,
    Set,
    TextIO,
    Tuple,
    Union,
    cast,
)
import subprocess
import re
import warnings


########################################
# CONSTANTS
########################################

# Number keys
ONEKEY     = (b'1')
TWOKEY     = (b'2')
THREEKEY   = (b'3')
FOURKEY    = (b'4')
FIVEKEY    = (b'5')
SIXKEY     = (b'6')
SEVENKEY   = (b'7')
EIGHTKEY   = (b'8')
NINEKEY    = (b'9')
ZEROKEY    = (b'0')

# Function keys
F1         = (b'^[OP')
F2         = (b'^[OQ')
F3         = (b'^[OR')
F4         = (b'^[OS')
F5         = (b'^[[15~')
F6         = (b'^[[17~')
F7         = (b'^[[18~')
F8         = (b'^[[19~')
F9         = (b'^[[20~')
F10        = (b'^[[21~')
F11        = (b'^[[23~')
F12        = (b'^[[24~')

UPARROW    = (b'\x1b[A')
DOWNARROW  = (b'\x1b[B')
RIGHTARROW = (b'\x1b[C')
LEFTARROW  = (b'\x1b[D')
BACKSPACE  = (b'\x7f')  # backspace/delete 
RETURN     = (b'\r')  # return/enter
FORMFEED   = (b'\x0c')  # ctrl+l
XMIT       = (b'\x04')  # ctrl+d
ETX        = (b'\x03')  # ctrl+c

## Colours (16 basic fg, 16 basic bg)
# Black
FGBLACK        = "\u001b[30m"
FGLIGHTBLACK   = "\u001b[30;1m"
BGBLACK        = "\u001b[40m"
BGLIGHTBLACK   = "\u001b[40;1m"
# Red
FGRED          = "\u001b[31m"
FGLIGHTRED     = "\u001b[31;1m"
BGRED          = "\u001b[41m"
BGLIGHTRED     = "\u001b[41;1m"
# Green
FGGREEN        = "\u001b[32m"
FGLIGHTGREEN   = "\u001b[32;1m"
BGGREEN        = "\u001b[42m"
BGLIGHTGREEN   = "\u001b[42;1m"
# Yellow
FGYELLOW       = "\u001b[33m"
FGLIGHTYELLOW  = "\u001b[33;1m"
BGYELLOW       = "\u001b[43m"
BGLIGHTYELLOW  = "\u001b[43;1m"
# Blue
FGBLUE         = "\u001b[34m"
FGLIGHTBLUE    = "\u001b[34;1m"
BGBLUE         = "\u001b[44m"
BGLIGHTBLUE    = "\u001b[44;1m"
# Magenta
FGMAGENTA      = "\u001b[35m"
FGLIGHTMAGENTA = "\u001b[35;1m"
BGMAGENTA      = "\u001b[45m"
BGLIGHTMAGENTA = "\u001b[45;1m"
# Cyan
FGCYAN         = "\u001b[36m"
FGLIGHTCYAN    = "\u001b[36;1m"
BGCYAN         = "\u001b[46m"
BGLIGHTCYAN    = "\u001b[46;1m"
# White
FGWHITE        = "\u001b[37m"
FGLIGHTWHITE   = "\u001b[37;1m"
BGWHITE        = "\u001b[47m"
BGLIGHTWHITE   = "\u001b[47;1m"
# Bold
BOLD           = "\u001b[1m"
# Underline
UNDERLINE      = "\u001b[4m"
# Reverse (Not text! Reverses the BG Colour!)
REVERSED       = "\u001b[7m"                                
# End of colour
EOC            = "\u001b[0m"


########################################
# ERRORS
########################################

'''
class Error(Exception):
    """Base class for other exceptions"""
    def __init__(self, errorName, codeInQuestion, fixes: Optional[str]=None, info: Optional[str]=None):
        self.errorName = errorName
        self.codeInQuestion = codeInQuestion
        self.fixes = fixes
        self.info = info

    def raise(self):
        print("Oops.. it seems an issue has occurred:\n"+self.errorName+"\n+-----------------------------------+")
        print("""
Code in question
`
%s
`
------------------------------------+""" % (self.codeInQuestion))
        if self.fixes != None:
            print("""
Potential fixes
`
%s
`
------------------------------------+""" % (self.fixes))
        if self.info != None:
            print("""
Has the issue been found
`

`
+-----------------------------------+""")    



class IllegalArgumentError(Error):
    """Called when a argument unbeknown to us gets passed"""
    pass
'''


########################################
# INDICATOR
########################################

class indicator:
    def parse(rawCharacter):
        return str(rawCharacter).replace("b", "", 1).replace("'", "")


    class arrow:
        """
        Stores what an arrow means. This allows the end user to type `arrow.up` and let it be understood.
        """
        up = UPARROW
        down = DOWNARROW
        right = RIGHTARROW
        left = LEFTARROW
    

    class escape:
        """
        Store some extra escape chars. This allows the end user to type `arrow.up` and let it be understood
        """
        backspace = BACKSPACE
        enter = RETURN
        ctrl_d = FORMFEED
        xmit = XMIT
        etx = ETX
    

    class colour:
        class fg:
            # Black
            black = FGBLACK
            lightblack = FGLIGHTBLACK
            # Red
            red = FGRED 
            lightred = FGLIGHTRED 
            # Green
            green = FGGREEN  
            lightgreen = FGLIGHTGREEN 
            # Yellow
            yellow = FGYELLOW  
            lightyellow = FGLIGHTYELLOW 
            # Blue
            blue = FGBLUE    
            lightblue = FGLIGHTBLUE  
            # Magenta
            magenta = FGMAGENTA    
            lightmagenta = FGLIGHTMAGENTA 
            # Cyan
            cyan = FGCYAN
            lightcyan = FGLIGHTCYAN
            # White
            white = FGWHITE 
            lightwhite = FGLIGHTWHITE 
 

        class bg:
            # Black
            black = BGBLACK
            lightblack = BGLIGHTBLACK 
            # Red
            red = BGRED  
            lightred = BGLIGHTRED
            # Green
            green = BGGREEN  
            lightgreen = BGLIGHTGREEN 
            # Yellow
            yellow = BGYELLOW  
            lightyellow = BGLIGHTYELLOW 
            # Blue
            blue = BGBLUE 
            lightblue = BGLIGHTBLUE 
            # Magenta
            magenta = BGMAGENTA
            lightmagenta = BGLIGHTMAGENTA
            # Cyan
            cyan = BGCYAN  
            lightcyan = BGLIGHTCYAN  
            # White
            white = BGWHITE  
            lightwhite = BGLIGHTWHITE 
        

        class formatting:
            # Bold
            bold = BOLD
            # Underline
            underline = UNDERLINE
            # Reverse (Not text! Reverses the BG Colour!)
            reverse = REVERSED                          
            # End of colour
            eoc = EOC


########################################
# GETCH
########################################

class Getch:
    """
    Getch (Get character) will grab an input from the user. Taking in 3 characters max! Getch gets satisfied in one button press, this
    allows capturing of single key presses but still allowing escape characters, or any escape character under 3 characters I.e. ^C
    """
    def __call__(self):
        """
        :rtype: class bytes
        :return: Returns character(s) pressed
        """
        fd = sys.stdin.fileno()  # Check if output medium is a terminal
        settings = termios.tcgetattr(fd)  # Gets file descripter attributes
        try:
            tty.setraw(sys.stdin.fileno())  # Set file descripter (In this case terminal) to raw
            ch = sys.stdin.buffer.raw.read(3)  # Reads 3 chars
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, settings)  # Set the tty attributes for file descriptor
        
        # This is not needed. It's here to make 100% sure a quit failsafe is implemented.
        if ch == ETX:
            raise KeyboardInterrupt("Default failsafe (ctrl+c)")
        return ch


########################################
# CURSOR
########################################

class Cursor:
    """
    Terminal cursor.
    """
    def __init__(self, posx, posy, visibility: Optional[bool]=True):
        """ 
        Constructor to initialize the object
        
        :param int posx: Begining x position for cursor
        :param int posy: Begining y position for cursor
        :param bool visibility: True = Shown, False = Hidden
        """
        self.posx = posx
        self.posy = posy
        self.visibility = visibility
        if self.visibility:
            self.changeVisibility(True)
        else:
            self.changeVisibility(False)


    def link(self):
        """
        Links cursor object to a screen object. This will auto restrict the cursor to the screen dimensions, if this is not what you are looking
        for set `linkCursor=False` when creating a Screen object!
        """
        pass


    def changeVisibility(self, visibility):
        """
        Changes the visibility of cursor

        :param bool visibility: True = Shown, False = Hidden
        """
        self.visibility = visibility
        if self.visibility:
            sys.stdout.write("\x1b[?25h")
        else:
            sys.stdout.write("\x1b[?25l")


    def getPos(self, xory: Optional[str]=None, updatePos: Optional[bool]=True):
        """
        Obtains position of cursor. This can be funky on some terminal emulators, for me my daily driver Terminator you must change up some
        settings to get this code to work! This may be the same for your end-user. Make sure you keep this in mind while using getPos()!
        
        :param str xory: Choose what to return "x", or "y". Default None (Meaning it will return both x and y)
        :param bool updatePos: Auto Updates cursor position after fetching row and col. Default is True

        :rtype: tuple of int's
        :return: Returns (column, row)
        """
        OldStdinMode = termios.tcgetattr(sys.stdin)
        settings = termios.tcgetattr(sys.stdin)
        settings[3] = settings[3] & ~(termios.ECHO | termios.ICANON)  # Disable echo, and stop the terminal from waiting for key press
        termios.tcsetattr(sys.stdin, termios.TCSAFLUSH, settings)
        try:
            temp = ""
            sys.stdout.write("\x1b[6n")  # Write mouse position silently
            sys.stdout.flush()  # Allows the write() code above this line to be read
            # ESC[hight;widthR
            while not (temp := temp + sys.stdin.read(1)).endswith('R'):  # If you are confussed on this look at stackoverflow.com/questions/26000198/what-does-colon-equal-in-python-mean
                pass
            res = re.match(r".*\[(?P<y>\d*);(?P<x>\d*)R", temp)  # Creates groups for values using regex
        finally:
            termios.tcsetattr(sys.stdin, termios.TCSAFLUSH, OldStdinMode)  # Re-enables "echo"
        if res:
            if updatePos:
                self.posx = res.group("x")
                self.posy = res.group("y")
            if xory == None:
                return (int(res.group("x")), int(res.group("y")))  # Returns (x, y)
            elif xory == "x":
                return int(res.group("x"))
            elif xory == "y":
                return int(res.group("y"))
            else:
                raise IllegalArgumentError('"%s" is an illegal argument!' % (xory) + " Come on dude... it's in the variable name..")


    def setPos(self, x, y):
        """
        Sets the position of cursor. If you are looking for changing the value and not setting the value look towards .move().

        :param int x: x position to set
        :param int y: y position to set
        """
        self.posx = x
        self.posy = y
        sys.stdout.write('\033[%s;%sH' % (self.posy, self.posx))        

    
    def returnPos(self):
        """
        """
        return (self.posx, self.posy)


    def move(self, x, y):
        """
        Changes the position of the cursor. If you are looking to set the value and not change the value look towards .setPos().

        :param int x: x position to change
        :param int y: y position to change
        """
        self.posx = x
        self.posy = y
        if self.posx >= 0:  # +
            sys.stdout.write('\x1b[%sC' % (self.posx))
        else:  # -
            sys.stdout.write('\x1b[%sD' % (int(str(self.posx)[1:])))  # Removes negative number with splicing
        
        if self.posy >= 0:  # +
            sys.stdout.write('\x1b[%sB' % (self.posy))
        else:  # -
            sys.stdout.write('\x1b[%sA' % (int(str(self.posy)[1:])))  # Removes negative number with splicing
        sys.stdout.flush()  # Update line


    def align(self, position):
        """
        Align cursor position with preset position E.g. "left" will put the cursor to the left side. "tright" will place the cursor in the
        top right of the screen

        :param string position: The position to go to I.e. 
                                           "tleft" "tmiddle" "tright"
                                            "left" "middle" "right"
                                           "bleft" "bmiddle" "bright"
        """
        # Align still needs to be finished. With the knowledge and stuff implemented now this can be done right! I will get around to this...
        # That is when I need the cursor.align function..

        if position=="left":
            self.move(-999, 0)
        elif position=="right":
            self.move(999, 0)


########################################
# SCREEN
########################################

class Screen:
    def __init__(self, cursor, height: Optional[int]=None, width: Optional[int]=None, linkCursor: Optional[bool]=False, autoCalibrate: Optional[bool]=True):
        self.terminal = sys.stdout  # Allows us to track printed text
        self.cachedScreen = ""
        self.cursor = cursor
        if autoCalibrate:
            self.height = self.getDimensions(returnFormat="y") if height == None else height
            self.width = self.getDimensions(returnFormat="x") if width == None else width
        else:
            self.height = height
            self.width = width
        
        if linkCursor:
            # Link cursor to screen
            self.cursor.link()


    ###
    # STDOUT REDIRECT
    ###
    
    def write(self, message):
        self.terminal.write(message)
        self.cachedScreen += message
    

    def read(self, n: int=...) -> str:
        sys.__stdout__.read(n)


    def flush(self) -> None:
        # this flush method is needed for python 3 compatibility.
        # this handles the flush command by running flush via old options.
        sys.__stdout__.flush()


    ###          
    # END OF REDIRECT
    ###


    def setBorder(self, theme={"topLeftCorner": "+", "botLeftCorner": "+", "topRightCorner": "+", "botRightCorner": "+", "connections": "-"}):
        pass


    def returnDimensions(self, returnFormat: Optional[str]="WxH"):
        """
        Returns current set dimentions for screen object. To update dimentions or fetch new ones use getDimensions().

        :param str returnFormat: The format in which to be retuned in
        """
        if returnFormat == "WxH":
            return str(self.width)+"x"+str(self.height)


    def getDimensions(self, returnFormat: Optional[str]="WxH", clearScreen: Optional[bool]=True, xory: Optional[str]=None, positiveyLimit: Optional[int]=None, negativeyLimit: Optional[int]=None, positivexLimit: Optional[int]=None, negativexLimit: Optional[int]=None):
        """
        Gets current screen dimentions using a funny little trick. No this does not use SIGWINCH but output will be the same never the less.
        Smart code has been implemented to auto create a positiveyLimit, this can be removed by setting a value to positiveyLimit.
        :param str returnFormat: The format in which to be retuned in
        :param bool clearScreen: If false screen will not be cleared when checking dimentions. This can cause some weird visual bugs if not expected and delt with manuly!!
        :param string xory: If "x" the returned value just be x and vice versa. If xory equal to NoneType then x and y will be returned.
        :param int positiveyLimit: This will set the dimentions limit on positive y direction
        :param int negativeyLimit: This will set the dimentions limit on negative y direction
        :param int positivexLimit: This will set the dimentions limit on positive x direction
        :param int negativexLimit: This will set the dimentions limit on negative x direction
        
        :rtype: Return varies depending on the value of `xory` but by default a tuple will be returned.
        :return: Return varies depending on the value of `xory` but by default (x, y) will be returned.
        """
        if clearScreen:
            os.system("clear")
        
        # Get init position
        initPos = self.cursor.getPos()
        
        # Get +y 
        posY = self.cursor.move(0, 999)
        posY = self.cursor.getPos("y", False)
        
        # Move back to init position
        self.cursor.setPos(initPos[0], initPos[1])
        
        # Get -y
        negY = self.cursor.move(0, -999)
        negY = self.cursor.getPos("y", False)
        
        # Move back to init position
        self.cursor.setPos(initPos[0], initPos[1])
        
        # Get +x (also known as right)
        posX = self.cursor.move(999, 0)
        posX = self.cursor.getPos("x", False)
        
        # Move back to init position
        self.cursor.setPos(initPos[0], initPos[1])
        
        # Get -x (also known as left)
        negX = self.cursor.move(-999, 0)
        negX = self.cursor.getPos("x", False)
 
        # Move back to init position
        self.cursor.setPos(initPos[0], initPos[1])
        
        if returnFormat == "WxH":
            return str(posX)+"x"+str(negY)
        
        elif returnFormat == "HxW":
            return str(posX)+"x"+str(negY)
        
        elif returnFormat == "xy":
            return (posX, negY)
        
        elif returnFormat == "yx":
            return (negY, posX)
 
        elif returnFormat == "x":
            return int(posX)

        elif returnFormat == "y":
            return int(negY)

        elif returnFormat == None:
            return posY, negY, posX, negX
        
        else:
            return posY, negY, posX, negX


    def setDimensions(self, x, y):
        pass


    def wipe(self):
        """
        Cleans off screen of all text. Be warned this also cleans the cachedScreen variable, if needed you may save cachedScreen to another
        variable... It's a double cache how fun!!
        """
        self.cachedScreen = ""
        os.system("clear")


# I could reposition this in the code, this is after I know what requires the Chunk object.
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
        # This MUST be re-worked! The amount of quirks I had to deal with in this is CRAZY!! 

        # Move cursor to ending chunk position
        cursor.setPos(self.position[2]+1, self.position[0])
        # Delete chunk
        for i in range(self.position[1], self.position[2]):
            sys.stdout.write("\b")
            sys.stdout.write(" ")
            sys.stdout.write("\b")
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
        """
        return self.position



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
            sys.exit(indicator.colour.formatting.bold+indicator.colour.formatting.underline+"Hey it seems you did not pass a screen object... You have passed a '%s' object" % (type(screen)))

        # Check for regex
        try:
            # Do some manual checks for re
            if pattern.isspace():
                raise re.error("Falsely raised error")
            isRe = re.compile(pattern)
        except re.error:
            isRe = False
        
        if isRe:
            pass
        else:
            # Uses "".split() to split string (Taking the easy way out.. this code is subject to change!)
            splitValue = (rawValue.split(pattern) if maxChunk == None else rawValue.split(pattern, maxChunk))
            # Remove random whitspace items in splitValue
            removeSpace = [x.strip(' ') for x in splitValue]
            deleteEmpty = [item for item in removeSpace if item.strip()]
            splitValue = deleteEmpty
            # Convert list of strings to a list of chunk objects
            for index, item in enumerate(splitValue):
                # Get positions of items on screen
                for match in re.finditer(splitValue[index], rawValue):  # A wee bit of re
                    position = (lineNumber, match.start(), match.end())
                splitValue[index] = Chunk(position, item)
            return splitValue


########################################
# TERMINAL
########################################

class Terminal:
    """Glues Screen, Line, Cursor into one object"""
    def __init__(self, screen, line, cursor):
        self.screen = screen
        self.line = line
        self.cursor = cursor


########################################
# CAPTURE KEY
########################################

def captureKey():
    """
    captureKey just takes Getch() and makes it usable by an end user.
    
    :rtype: class bytes
    :return: Returns key press
    """
    keyPressed = Getch()
    while True:
        key = keyPressed()
        if key != '':
            break
    if key==ETX:
        raise KeyboardInterrupt("Default failsafe (ctrl+c)")
    return key


########################################
# CAPTURE INPUT
########################################

def captureInput(blind: Optional[bool]=False, limit: Optional[int]=9223372036854775807):
    """
    captureInput will take the users key presses until a specified length is hit or enter key is pressed
    
    :param bool blind: If true input will not be shown when typing. Default is false
    :param int limit: You may set a limit to the number of characters that can be used. Good for passwords and such. Default is 9223372036854775807
    :rtype: String
    :return: Returns a string (String is used to ignore escape characters and ANSI in general.. also it makes my life easy...)
    """
    stringToReturn = ""
    cursor = Cursor(0, 0)
    while True:
        # Make sure limit if supplied is met
        if len(stringToReturn) >= limit:
            break # Making a more customizable system would be nice
        key = captureKey()
        if key == RIGHTARROW:
            cursor.move(1, 0)
            continue
        elif key == LEFTARROW:
            cursor.move(-1, 0)
            continue
        elif key == UPARROW:
            continue
        elif key == DOWNARROW:
            continue
        elif key == BACKSPACE:
            stringToReturn = stringToReturn[0:-1]  # Remove character from final return string
            sys.stdout.write("\b")  # Backup a character
            sys.stdout.write(" ")  # Replace character with blankspace
            sys.stdout.write("\b")  # Move back the cursor again.
            sys.stdout.flush()  # Refresh line
            continue  # Loop back the while loop (Stops the program from registering backspace escape code)
        elif key == RETURN:
            break
        if blind:
            stringToReturn+=str(key).replace("b", "", 1).replace("'", "")
        else:
            sys.stdout.write(str(key).replace("b", "", 1).replace("'", ""))
            sys.stdout.flush()
            stringToReturn+=str(key).replace("b", "", 1).replace("'", "")
    
    print("", end="\n")  # Fixes next print printing on same line.
    return stringToReturn


########################################
# START
########################################

def init():
    """Automaticly setups reter for user"""
    cursor = Cursor(0, 0)
    screen = Screen(cursor)
    line = Line(cursor)
    sys.stdout = screen
    terminal = Terminal(screen, line, cursor)
    return terminal


########################################
# MAIN - FOR DEBUGGING REASONS
########################################

def main():
    terminal = init()
    print("The quick brown fox")
    print("Cool beans")
    chunks = terminal.line.chunkIt(terminal.screen, " ", 1)
    chunks[0].setColour(terminal.cursor, bg=indicator.colour.formatting.reverse)
    chunks[0].move(terminal.cursor, 0, 2)


########################################
# RUN - FOR DEBUGGING REASONS
########################################

if __name__=='__main__':
    main()


