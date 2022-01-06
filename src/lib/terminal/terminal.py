import os
import sys
import termios
import tty
from lib.terminal.screen import Screen, Line
from lib.cursor.cursor import Cursor 
from lib.event.input.keyboard.keyboard import Keyboard
from lib.errhandler.errors import UnexpectedResult
from typing import Optional


########################################
# TERMINAL
########################################

class Terminal:
    """Terminal manipulation object"""
    def __init__(self):
        """Constructor to initialize object"""
        self.MEMORY = {}


    ###################
    # Quick start
    ###################
    def quick_start(self) -> object:
        """
        Creates a Terminal object quickly, and in a unconfigurable manner. Good as long you don't need to over customize a TC object. Will also validate tty.

        :rtype: object
        :return: Returns Terminal object with all TC objects pre-connected
        """
        if self.is_valid_tty():
            cursor = Cursor(0, 0)
            screen = Screen(cursor)
            line = Line(cursor)
            keyboard = Keyboard(cursor)
            self.connect(screen, line, cursor, keyboard)
            return self
        else:
            raise ValueError("Cannot start a Terminal object. (It seems the output medium is not a valid terminal, are you using a terminal?)")


    ###################
    # Cache tc attr
    ###################
    def cache_tc_attr(self):
        """
        Cache terminal attributes to memory
        """
        if self.is_valid_tty():  # Make sure tty is valid
            self.MEMORY.update({"tcattr":self.get_tc_attr()})  # Update in memory
        else:
            print("Failed to cache tcattr. (It seems output medium is not a terminal, are you using a terminal?)")


    ###################
    # Is tty?
    ###################
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
    

    ###################
    # Is valid tty?
    ###################
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

    
    ###################
    # Set tc attr
    ###################
    def set_tc_attr(self):
        """
        Set the TC attributes, don't mess around with this unless you know what you are doing! A good amount of knowledge is needed to use this function.
        """
        pass
    

    ###################
    # Get tc attr
    ###################
    def get_tc_attr(self):
        """
        Obtains terminal control (TC) attributes

        :rtype: list
        :returns: Returns TCATTR's
        """
        if self.is_valid_tty():  # Make sure tty is valid
            fd = sys.stdout.fileno()  # Get file descripter
            return termios.tcgetattr(fd)  # Get & return terminal attributes
        else:
            return "Failed to get tcattr. (It seems output medium is not a terminal, are you using a terminal?)"


    ###################
    # Connect
    ###################
    def connect(self, screen, line, cursor, keyboard: Optional[object]=None):
        """
        Connects abstract terminal control (TC) objects into one object connected to a single terminal. 
        """
        self.screen, self.line, self.cursor = screen, line, cursor
        if keyboard != None:
            self.keyboard = keyboard



