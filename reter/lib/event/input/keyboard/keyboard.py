########################################
# IMPORTS
########################################

import termios
import tty
import sys
from reter.lib.event.input.map.keys import *
from reter.lib.cursor.cursor import Cursor  # I could remove this dependency.. 
from reter.lib.style.indicator import indicator
from typing import Optional


########################################
# KEYBOARD
########################################

class Keyboard:
    def __init__(self, screen, line, cursor):
        self.screen = screen
        self.line = line
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
        return_string = ""  # The final string to return
        char_list = []  # A list of every character
        pointer = 0  # Tells us where we are on the string (And screen in general)
        
        self.cursor.set_pos(0, 0)
        # Allows us to keep compatibility between terminals
        width_max = self.screen.width
        while True: 
            key = self.capture_key()
            # Check if enter has been pressed
            if key == indicator.escape.enter:
                break
            
            elif key == indicator.arrow.left:  # Allows for moving around the string
                if self.cursor.get_pos()[0] != 1:  # Check if we are too far left
                    pointer -= 1
                self.cursor.move(-1, 0)
                continue
            
            elif key == indicator.arrow.right: # Allows for moving around the string
                if self.cursor.get_pos()[0] != width_max:  # Check if we are too far right
                    pointer += 1
                self.cursor.move(1, 0)
                continue
            
            elif key == indicator.escape.backspace:
                _current_column = self.cursor.get_pos()[0]  # Do it once, optimizing this code!

                if _current_column != 1:  # Make sure we aren't too far left
                    pointer -= 1
                else:
                    continue
                
                #### Do the deleting visually ####
                ## :WARNING: This function is heavy on some terminals, I.e. Terminator, Gnome-Terminal.
                ## :OPTIMISE: This code needs some serious optimizing, it works just fine on basic terminals
                ##            but, that's not good enough. I want this code to run good on terminals that are Gnome based and such
                _look_ahead = char_list[pointer+1:]
                self.cursor.move(len(_look_ahead), 0)
                print("\b \b"*(len(_look_ahead)+1), end="", flush=True)
                _temp_pos = self.cursor.get_pos()
                print("".join(_look_ahead), end="", flush=True)
                self.cursor.set_pos(_temp_pos[0], _temp_pos[1])
                #################################
                
                #### Do the deleting internally ####
                ## We do the deleting AFTER doing it visually, this stops weird conflict
                if len(char_list) >= _current_column-1:  # Check if we are on a character
                    # We minus _current_column by two so we comply with index format 0.. not 1..
                    # Now why not one? Well _current_column returns column+1 to comply with the 
                    # terminal. Meaning we have to -2, to get the correct format!
                    char_list.pop(_current_column-2)  # Do the deleting internally
                ####################################
                continue

            else: # Just a normal key press
                # We grab length here, this is because a key like ctrl+d
                # Would write many characters at once. This small addition
                # fixes that.
                pointer += len(indicator.parse(key, True))
            
            char_list.append(indicator.parse(key, True))
            print(indicator.parse(key, True), end="", flush=True)
        # Create a string using char_list
        for c in char_list:
            return_string += c
        print("", end="\n", flush=True)  # Fixes a newline issue
        return return_string
