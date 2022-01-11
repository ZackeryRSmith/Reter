import os
import sys
import termios
import tty
import signal
from reter.lib.terminal.screen import Screen, Line
from reter.lib.cursor.cursor import Cursor 
from reter.lib.event.input.keyboard.keyboard import Keyboard
from reter.lib.errhandler.errors import UnexpectedResult
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
# OUTPUT REDIRECT
########################################
class OutputRedirect(object):
    """Built-in object for stdout redirects"""
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

    def write(self, s: AnyStr, dc: Optional[bool]=False, flush: Optional[bool]=True):
        """
        Just the stdout write function, but with a capturing system

        :: IMPORTANT
        : Make sure you add "\\n" to the end of your string, if you don't visual bugs will occur. 
        : I am working on fixing this bug, and no it's not "simple" or else it would be fixed already.
        : Feel free to give it a shot, open a pull request.
        
        :: RECOMENDATION
        : Use print(), it passes through this function and adds a newline character for you. If you MUST use stdout.write() make sure you read
        : the `IMPORTANT` section found above!
        
        :param str s: String to write
        :param bool dc: if dc (Don't cache) is True, output will be shown on the screen (to the user), but the written line won't show in the cached_buffer variable. This can cause issues, this parameter should be left untouched, unless you know what you are doing. 
        :param bool flush: Flushes buffer to output no matter what
        """
        if dc != True:  # If dc (don't cache) is false, it means we will cache the string
            self.cached_buffer += s
        sys.__stdout__.write(str(s))
        if flush:
            sys.__stdout__.flush()

    def writelines(self, lines: Iterable[AnyStr], dc: Optional[bool]=False):
        """
        Just the stdout writelines function, but with a capturing system
        
        :param str lines: A list of strings
        :param str dc: if dc (Don't cache) is True, output will be shown on the screen (to the user), but the written line won't show in the cached_buffer variable. This can cause issues, this parameter should be left untouched, unless you know what you are doing. 
        """
        if dc != True:  # If dc (don't cache) is false, it means we will cache the string
            for line in lines:
                self.cached_buffer += line
        sys.__stdout__.writelines(lines)
    
    def writable(self) -> bool:
        """
        Check if stdout is writable

        :rtype: bool
        :return: True, or False
        """
        return sys.__stdout__.writable()

    def isatty(self) -> bool:
        """
        Check if stdout is connected to a tty

        :rtype: bool
        :return: True, or False
        """
        return sys.__stdout__.isatty()

    def fileno(self) -> int:
        """
        Get file descripter

        :rtype: int
        :return: File descripter 0, 1, or 2
        """
        return sys.__stdout__.fileno()

    def flush(self):
        """
        Flush everything, meaning that it will write everything in the buffer to the terminal, even if normally it would wait before doing so
        """
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
        Creates a Terminal object quickly, and in a unconfigurable manner. Good as long you don't need to over customize a TC object.

        :rtype: object
        :return: Returns Terminal object with all TC objects pre-connected
        """
        if self.is_valid_tty():
            self.create_alt_buffer()  # Create buffer
            signal.signal(signal.SIGWINCH, self.resize_handler)
            output = OutputRedirect()
            self.redirect_stdout(output)
            cursor = Cursor(0, 0)
            screen = Screen(cursor, clear_screen=False)
            line = Line(cursor)
            keyboard = Keyboard(screen, line, cursor)
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
    # Resize handler
    ###################
    def resize_handler(self, signum, frame):
        # This does work... thing is I am having a *great* time getting
        # this to a end-user usable state. I could just fix resizing issues
        # within this function by default. But, I want a end user to tell when
        # their window has been resized.
        pass


    ###################
    # Set mode
    ###################
    def set_mode(self, m: AnyStr):
        """
        Set terminal in 'raw', or 'cbreak' mode.
        
        :param str mode: The mode to set for terminal I.e. 'raw', or 'cbreak'
        """
        if m == "raw":
            self.fd = sys.stdin.fileno()
            self.saved_settings = termios.tcgetattr(self.fd)
            tty.setraw(self.fd)
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
    def set_tc_attr(self, fd: int, when: int, attributes: list):
        """
        Set the TC attributes, don't mess around with this unless you know what you are doing! A good amount of knowledge is needed to use this function.
        
        :param int fd: File descripter
        :param int when: When should change shall occur I.e. "TCSANOW", "TCSADRAIN", "TCSAFLUSH". More info at https://stackoverflow.com/questions/49684768/tcsetattr-what-are-the-differences-between-tcsanow-tcsadrain-tcsaflush-and
        """
        termios.tcsetattr(fd, when, attributes)  # Set attributes
    

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
