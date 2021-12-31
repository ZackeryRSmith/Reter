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

# Terminal info
__terminal_emulator__ = None  # Set once reter is initialized
__terminal__ = None  # Set once reter is initialized





########################################
# ERRORS
########################################

class Error(Exception):
    """Base class for other exceptions"""
    def __init__(self, errorName, codeInQuestion, fixes: Optional[str]=None, info: Optional[str]=None):
        self.errorName = errorName
        self.codeInQuestion = codeInQuestion
        self.fixes = fixes
        self.info = info
        print(FGRED+"Oops.. it seems an issue has occurred:\n\n"+EOC+FGRED+self.errorName+FGYELLOW+"\n+-----------------------------------+"+EOC)
        print("""
%sCode in question
%s`
%s
`%s
%s------------------------------------+""" % (FGYELLOW, FGCYAN, self.codeInQuestion, EOC, FGYELLOW))
        if self.fixes != None:
            print("""
%sPotential fixes
%s`
%s
`%s
%s------------------------------------+""" % (FGYELLOW, FGCYAN, self.fixes, EOC, FGYELLOW))
        if self.info != None:
            print("""
%sAdditional info
%s`
%s
`%s""" % ((FGYELLOW, FGCYAN, self.info, EOC)))
        print("%s+-----------------------------------+%s" % (FGYELLOW, EOC))    



class IllegalArgumentError(Error):
    """Called when a argument unbeknown to us gets passed"""
    pass



########################################
# GETCH
########################################

class Getch:
    """
    Getch (Get character) will grab an input from the user. Taking in 3 characters max! Getch gets satisfied with one button press, this
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


# I think we can keep this with maybe a rename of the class or put this under terminal.py (Not yet implemented but found in /terminal/)
########################################
# TERMINAL
########################################

class Terminal:  # Name has to be changed, or something needs to happen here
    """Glues Screen, Line, Cursor into one object as well as updating terminal info"""
    def __init__(self, screen, line, cursor):
        self.screen = screen
        self.line = line
        self.cursor = cursor

        # Get terminal, and terminal emulator
        __terminal_emulator__ = subprocess.check_output('basename "/"$(ps -f -p $(cat /proc/$(echo $$)/stat | cut -d \  -f 4) | tail -1 | sed '+"'s/^.* //')", shell=True)  # Get terminal emulator


# Will be put in /terminal/
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


# Will be put in /terminal/
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
        if key == indicator.arrow.right:
            cursor.move(1, 0)
            continue
        elif key == indicator.arrow.left:
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


# Will most likly stay in this path
########################################
# INIT
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
    #print("The quick brown fox")
    #print("Cool beans")
    #chunks = terminal.line.chunkIt(terminal.screen, " ", 1)
    #chunks[0].setColour(terminal.cursor, bg=indicator.colour.formatting.reverse)
    #chunks[0].move(terminal.cursor, 0, 2)
    print(captureInput())


########################################
# RUN - FOR DEBUGGING REASONS
########################################

if __name__=='__main__':
    main()


