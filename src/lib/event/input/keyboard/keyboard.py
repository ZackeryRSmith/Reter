########################################
# IMPORTS
########################################

import termios
import tty
import sys
from src.lib.event.input.map.keys import *
from src.lib.cursor.cursor import Cursor  # I could remove this dependency.. 
from src.lib.style.indicator import indicator
from typing import Optional


########################################
# KEYBOARD
########################################

class Keyboard:
    def __init__(self, cursor):
        self.cursor = cursor
        
        
    ###################
    # Getch
    ###################
    def getch(self):
        """
        Getch (Get character) will grab an input from the user. Taking in 3 characters max! Getch gets satisfied with one button press, this
        allows capturing of single key presses but still allowing escape characters, or any escape character under 3 characters I.e. ^C
                    
        :rtype: class bytes
        :return: Returns character(s) pressed
        """
        fd = sys.stdin.fileno()  # Gets file descripter
        settings = termios.tcgetattr(fd)  # Gets fd attributes
        try:
            tty.setraw(sys.stdin.fileno())  # Set file descripter (In this case terminal) to raw
            ch = sys.stdin.buffer.raw.read(3)  # Reads 3 chars
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, settings)  # Set the tty attributes for file descriptor
            
        if ch == ETX:
            raise KeyboardInterrupt("Default failsafe (ctrl+c)")
        return ch


    ###################
    # Capture key
    ###################
    def capture_key(self):
        """
        capture_key just takes Getch() and makes it usable by an end user.
        
        :rtype: class bytes
        :return: Returns key press
        """
        key_pressed = self.getch
        while True:
            key = key_pressed()
            if key != '':
                break
        # This is not needed. It's here to make 100% sure a quit failsafe is implemented.
        if key==ETX:
            raise KeyboardInterrupt("Default failsafe (ctrl+c)")
        return key


    ########################################
    # CAPTURE INPUT
    ########################################

    def capture_input(self, blind: Optional[bool]=False, limit: Optional[int]=9223372036854775807):
        """
        captureInput will take the users key presses until a specified length is hit or enter key is pressed

        :param bool blind: If true input will not be shown when typing. Default is false
        :param int limit: You may set a limit to the number of characters that can be used. Good for passwords and such. Default is 9223372036854775807
        :rtype: String
        :return: Returns a string (String is used to ignore escape characters and ANSI in general.. also it makes my life easy...)
        """
        stringToReturn = ""
        self.cursor.setPos(0, 0)  # Could fix this to receive a terminal object
        while True:
            # Make sure limit if supplied is met
            if len(stringToReturn) >= limit:
                break # Making a more customizable system would be nice
            key = self.capture_key()
            if key == indicator.arrow.right:
                self.cursor.move(1, 0)
                continue
            elif key == indicator.arrow.left:
                self.cursor.move(-1, 0)
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

