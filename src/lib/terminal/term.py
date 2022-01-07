import os
import sys
import termios
import tty
from lib.terminal.screen import Screen, Line
from lib.cursor.cursor import Cursor 
from lib.event.input.keyboard.keyboard import Keyboard
from lib.errhandler.errors import UnexpectedResult
from typing import (
    Any,
    AnyStr,
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


########################################
# TERMINAL
########################################
class OutputRedirect(object):
    def __init__(self):
        self.name = sys.__stdout__.name  # Redirect name ("stdout" in most cases)
        self.mode = sys.__stdout__.mode  # Current mode
        self.errors = sys.__stdout__.errors  # Error type
        self.encoding = sys.__stdout__.encoding  # stdout current encoding
        self.closed = sys.__stdout__.closed  # Is closed?
        self.buffer = sys.__stdout__.buffer  # Current buffer
        self.line_buffering = sys.__stdout__.line_buffering  # Is line_buffering?
        self.newlines = sys.__stdout__.newlines  # Is newlines?
        self.cached_buffer = ""  # Cached screen variable

    def write(self, s: AnyStr):
        """
        Just standard out but with a capturing system

        :: IMPORTANT
        : Make sure you add "\\n" to the end of your string, if you don't visual bugs will occur. 
        : I am working on fixing this bug, and no it's not "simple" or else it would be fixed already.
        : Feel free to give it a shot, open a pull request.
        
        :: RECOMENDATION
        : Use print(), it passes through this function and adds a newline character for you. If you MUST use stdout.write() make sure you read
        : the `IMPORTANT` section found above!
        
        :param str s: String to write
        """
        self.cached_buffer += s
        sys.__stdout__.write(str(s))
    
    def writelines(self, lines: Iterable[AnyStr]):
        for line in lines:
            self.cached_buffer += line
        sys.__stdout__.writelines(lines)

    def writable(self) -> bool:
        sys.__stdout__.writable()

    def isatty(self) -> bool:
        sys.__stdout__.isatty()

    def fileno(self) -> int:
        sys.__stdout__.fileno()

    def flush(self):
        sys.__stdout__.flush()


########################################
# TERMINAL
########################################

class Terminal:
    """Terminal manipulation object"""
    def __init__(self):
        """Constructor to initialize object"""
        self.fd = sys.stdout.fileno()
        self.saved_settings = termios.tcgetattr(self.fd)
        self.MEMORY = {}

    
    # Documented | txt | 0.1b
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
            self.create_alt_buffer()  # Create buffer
            output = OutputRedirect()
            self.redirect_stdout(output)
            cursor = Cursor(0, 0)
            screen = Screen(cursor, clear_screen=False)
            line = Line(cursor)
            keyboard = Keyboard(cursor)
            self.connect(screen, line, cursor, keyboard, output)
            return self
        else:
            raise ValueError("Cannot start a Terminal object. (It seems the output medium is not a valid terminal, are you using a terminal?)")


    ###################
    # Redirect stdout
    ###################
    def redirect_stdout(self, o: object):
        """
        Redirect stdout to an object, to go back to default pass in sys.__stdout__
        """
        sys.stdout = o


    ###################
    # Set mode
    ###################
    def set_mode(self, m: AnyStr):
        """
        !:! NOT FINISHED !:!
        
        Set terminal in 'raw', 'cooked', or 'cbreak' mode.
        
        :param str mode: The mode to set for terminal I.e. 'raw', 'cooked', or 'cbreak'
        """
        if m == "raw":
            pass
        elif m == "cooked":
            pass
        elif m == "cbreak":
            self.fd = sys.stdin.fileno()
            self.saved_settings = termios.tcgetattr(self.fd)
            tty.setcbreak(self.fd)
        else:
            pass
    

    # Documented | txt | 0.1b
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


    # Documented | txt | 0.1b
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
    

    # Documented | txt | 0.1b
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
    

    # Documented | txt | v0.1b
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


    # Documented | txt | v0.1b
    ###################
    # Create alt buffer
    ###################
    def create_alt_buffer(self):
        """
        Creates, and activates an alternate buffer
        """
        sys.stdout.write("\033[?1049h\033[H")
        
    
    # Documented | txt | v0.1b
    ###################
    # exit
    ###################
    def exit(self):
        """
        Exits current screen buffer
        """
        sys.stdout.write("\033[?1049l")  # Restore screen
        termios.tcsetattr(self.fd, termios.TCSADRAIN, self.saved_settings)  # Restore old stdout settings


    # Documented | txt | v0.1b
    ###################
    # Connect
    ###################
    def connect(self, screen, line, cursor, keyboard: Optional[object]=None, output: Optional[object]=None):
        """
        Connects abstract terminal control (TC) objects into one object connected to a single terminal. 
        """
        self.screen, self.line, self.cursor = screen, line, cursor
        if keyboard != None:
            self.keyboard = keyboard
        if output != None:
            self.output = output
