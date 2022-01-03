import os
import sys
import termios
import tty
from lib.terminal.screen import Screen, Line
from lib.cursor.cursor import Cursor 
from lib.errhandler.errors import UnexpectedResult


class Terminal:
    def __init__(self):
        self.MEMORY = {}


    def quick_start(self):
        """
        Creates a Terminal object quickly, and in a unconfigurable manner. Good as long you don't need to over customize a TC object. Will also validate tty.

        :rtype: object
        :return: Returns Terminal object with all TC objects pre-connected
        """
        if self.is_valid_tty():
            terminal = Terminal()
            cursor = Cursor(0, 0)
            screen = Screen(cursor)
            line = Line(cursor)
            terminal.connect(screen, line, cursor)
            return terminal
        else:
            raise ValueError("Cannot start a Terminal object. (It seems the output medium is not a valid terminal, are you using a terminal?)")
            # Need to fix error system (And make it look better)
            #raise UnexpectedResult.UnexpectedResult("UnexpectedResult", "if self.is_valid_tty():", "Use a terminal", "Cannot quick start a Terminal object. (It seems the output medium is not a valid terminal, are you using a terminal?)")


    def cache_tc_attr(self):
        """
        Cache terminal attributes to memory
        """
        if self.is_valid_tty():  # Make sure tty is valid
            self.MEMORY.update({"tcattr":self.get_tc_attr()})  # Update in memory
        else:
            print("Failed to cache tcattr. (It seems output medium is not a terminal, are you using a terminal?)")


    def is_tty(self) -> bool:
        """
        Checks if output medium is a terminal

        :rtype: bool
        :return: Returns a True or False operator
        """
        fd = sys.__stdout__.fileno()  # Get file descripter
        if os.isatty(fd):  # Check if fd is a tty (Terminal)
            return True
        else: 
            return False
    

    def is_valid_tty(self) -> bool:
        """
        Checks if output medium is a terminal, if so then validate (Compatibility thing...)

        :rtype: bool
        :return: Returns a True or False operator 
        """
        fd = sys.__stdout__.fileno()  # Get file descripter
        if os.isatty(fd):
            settings = termios.tcgetattr(fd)  # Gets terminal attributes
            try:
                # Attempts to set attributes, if an error arose the tty is invalid.
                # Even if this line succeeds in execution it will do nothing, we
                # are just trying to set already set settings; setting already active
                # settings.
                termios.tcsetattr(sys.stdin, termios.TCSAFLUSH, settings)
                # If the line above executes it means we have a valid tty
                return True
            except:
               return False
        else:
            return False

    
    def set_tc_attr(self):
        pass
    

    def get_tc_attr(self):
        if self.is_valid_tty():  # Make sure tty is valid
            fd = sys.stdout.fileno()  # Get file descripter
            return termios.tcgetattr(fd)  # Get & return terminal attributes
        else:
            return "Failed to get tcattr. (It seems output medium is not a terminal, are you using a terminal?)"


    def connect(self, screen, line, cursor):
        """
        Connects abstract terminal control (TC) objects into one object connected to a single terminal. 
        """
        self.screen, self.line, self.cursor = screen, line, cursor
