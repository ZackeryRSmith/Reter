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
# End of color
EOC            = "\u001b[0m"



########################################
# ERRORS
########################################

class Error(Exception):  # Not currently being used but I see needs for this in the future.
    """Base class for other exceptions"""
    pass


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
    

    class color:
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
            # End of color
            eoc = EOC


########################################
# GETCH
########################################

class Getch:
    """
    Getch (Get character) will grab an input from the user. Taking in 3 characters max! This limit must be satisfied in one button press, this
    allows capturing of single key presses and escape character under 3 characters I.e. ^C
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
            sys.stdout.write("\x1b[?25h")
        else:
            sys.stdout.write("\x1b[?25l")


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


    def getPos(self):
        """
        Obtains position of cursor. This can be funky on some terminal emulators, for me my daily driver Terminator, you need to change up some
        setting to get this code to work! If a non-supported terminal is found in-use a diffrent method of getting mouse position will be used.
        
        :param bool updatePos: Auto Updates cursor position after fetching row and col

        :rtype: tuple of int's
        :return: Returns (column, row)
        """
        # \x1b[6n
        #sys.stdout.write("\033[6n")
        #rawPos = sys.stdin.buffer.raw.read(7)
        #cleanedPos = re.match(bytes('\[.*R', encoding='utf8'), rawPos)
        #finalPos = str(cleanedPos.group()).replace("[", "").replace(";", ",").replace("R", "", 1)
        OldStdinMode = termios.tcgetattr(sys.stdin)
        _ = termios.tcgetattr(sys.stdin)
        _[3] = _[3] & ~(termios.ECHO | termios.ICANON)
        termios.tcsetattr(sys.stdin, termios.TCSAFLUSH, _)
        try:
            _ = ""
            sys.stdout.write("\x1b[6n")
            sys.stdout.flush()
            while not (_ := _ + sys.stdin.read(1)).endswith('R'):
                True
            res = re.match(r".*\[(?P<y>\d*);(?P<x>\d*)R", _)
        finally:
            termios.tcsetattr(sys.stdin, termios.TCSAFLUSH, OldStdinMode)
        if(res):
            return (res.group("x"), res.group("y"))
            return (-1, -1)

        

    def setPos(self, x, y):
        """
        Sets the position of cursor. If you are looking for changing the value and not setting the value look towards .move().

        :param int x: x position to set
        :param int y: y position to set
        """
        self.posx = x
        self.posy = y
        sys.stdout.write('\033[%s;%sH' % (self.posx, self.posy))        


    def move(self, x, y):
        """
        Changes the position of the cursor. If you are looking to set the value and not change the value look towards .setPos().

        :param int x: x position to change
        :param int y: y position to change
        """
        self.posx = x
        self.posy = y
        if self.posx > 0:
            sys.stdout.write('\x1b[%sC' % (self.posx))
        elif self.posx < 0:
            sys.stdout.write('\x1b[%sD' % (int(str(self.posx)[1:])))  # Removes negative number with splicing
        
        if self.posy > 0:
            sys.stdout.write('\x1b[%sA' % (self.posy))
        elif self.posy < 0:
            sys.stdout.write('\x1b[%sB' % (int(str(self.posy)[1:])))  # Removes negative number with splicing
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
        if position=="left":
            self.move(-100, 0)
        elif position=="right":
            self.move(100, 0)


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
    :return: Returns a string (String is used to ignore escape characters and ANSI in general.. also maybe because it makes my life easy...)
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
# SCREEN
########################################

class Screen:
    def __init__(self, cursor, height: Optional[int]=None, width: Optional[int]=None):
        self.cursor = cursor
        self.height = self.getDimensions("y") if height == None else height
        self.width = self.getDimensions("x") if width == None else width

    def setBorder(self, theme={"topLeftCorner": "+", "botLeftCorner": "+", "topRightCorner": "+", "botRightCorner": "+", "connections": "-"}):
        pass

    def getDimensions(self, xory: Optional[str]=None, positiveyLimit: Optional[int]=None, negativeyLimit: Optional[int]=None, positivexLimit: Optional[int]=None, negativexLimit: Optional[int]=None):
        """
        Gets current screen dimentions using a funny little trick. No this does not use SIGWINCH but output will be the same never the less.
        Smart code has been implemented to auto create a positiveyLimit, this can be removed by setting a value to positiveyLimit.

        :param string xory: If "x" the returned value just be x and vice versa. If xory equal to NoneType then x and y will be returned.
        :param int positiveyLimit: This will set the dimentions limit on positive y direction
        :param int negativeyLimit: This will set the dimentions limit on negative y direction
        :param int positivexLimit: This will set the dimentions limit on positive x direction
        :param int negativexLimit: This will set the dimentions limit on negative x direction
        
        :rtype: int
        :return: Return varies depending on the value of `xory` but by default (x, y) will be returned.
        """
        pass

    def setDimensions(self, x, y):
        pass


########################################
# MAIN - FOR DEBUGGING REASONS
########################################

def main():
    cursor = Cursor(0, 0)
    print(cursor.getPos())

########################################
# RUN - FOR DEBUGGING REASONS
########################################

if __name__=='__main__':
    main()


