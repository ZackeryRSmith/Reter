########################################
# IMPORTS
########################################

import re
import sys
import os
from typing import Optional
from reter.lib.cursor.cursor import Cursor  


########################################
# SCREEN
########################################

class Screen:
    def __init__(self, cursor, height: Optional[int]=None, width: Optional[int]=None, link_cursor: Optional[bool]=False, auto_calibrate: Optional[bool]=True, clear_screen: Optional[bool]=True, wrap: Optional[bool]=True):
        """Constructor to initialize object"""
        self.cursor = cursor
        if auto_calibrate:
            self.height = (self.get_dimensions(return_format="lines") if clear_screen == True else self.get_dimensions(return_format="lines", clear_screen=False)) if height == None else height
            self.width = (self.get_dimensions(return_format="columns") if clear_screen == True else self.get_dimensions(return_format="columns", clear_screen=False)) if width == None else width
        else:
            self.height = height
            self.width = width
    
        if wrap:
            self.set_mode(7)  # Enable
        else:
            self.reset_mode(7)  # Disable

        # Does nothing as of now - Not needed really, will most likely be removed in final version
        if link_cursor:
            # Link cursor to screen
            self.cursor.link()


    def return_dimensions(self, return_format: Optional[str]="WxH", recalibrate_dimensions: Optional[bool]=True):
        """
        Returns current set dimensions for screen object. To update dimensions or fetch new ones use getDimensions().

        :param str return_format: The format in which to be retuned in
        """
        if return_format == "WxH":
            if recalibrate_dimensions:
                return self.get_dimensions("WxH")
        elif return_format == "HxW":
            if recalibrate_dimensions:
                return self.get_dimensions("HxW")
        else:
            pass


    def get_dimensions(self, return_format: Optional[str]="WxH", clear_screen: Optional[bool]=True):
        """
        Gets current screen dimensions
        
        :param str return_format: The format in which to be retuned in
        :param bool clear_screen: If false screen will not be cleared when checking dimensions. This can cause some weird visual bugs if not expected and dealt with manually!!
        
        :rtype: By default a string will be returned.
        :return: Return differs depending on the value of `return_format`. By default (Width x Height) will be returned.
        """
        if clear_screen:
            os.system("clear")
        terminal_size = os.get_terminal_size()
        self.width = terminal_size.columns
        self.height = terminal_size.lines
        if return_format == "CxL":
            return str(terminal_size.columns)+"x"+str(terminal_size.lines)

        elif return_format == "LxC":
            return str(terminal_size.lines)+"x"+str(terminal_size.columns)
        
        elif return_format == "cl":
            return (terminal_size.columns, terminal_size.lines)
        
        elif return_format == "lc":
            return (terminal_size.lines, terminal_size.columns)
        
        elif return_format == "columns":
            return terminal_size.columns
        
        elif return_format == "lines":
            return terminal_size.lines
        
        elif return_format == None:
            return (terminal_size.lines, terminal_size.columns)
        
        else:
            return (terminal_size.lines, terminal_size.columns)


    def set_mode(self, value):
        """
        Set screen width and type of screen

        :param int value: Uses value for presets defined by a terminal, read docs for more info. All presets are listed below
            * 0 : 40 x 25 monochrome (text)
            * 1 : 40 x 25 color (text)
            * 2 : 80 x 25 monochrome (text)
            * 3 : 80 x 25 color (text)
            * 4 : 320 x 200 4-color (graphics)
            * 5 : 320 x 200 monochrome (graphics)
            * 6 : 640 x 200 monochrome (graphics)
            * 7 : Enables line wrapping
            * 13 : 320 x 200 color (graphics)
            * 14 : 320 x 200 color (graphics)
            * 15 : 640 x 350 monochrome (2-color graphics)
            * 16 : 640 x 350 color (16-color graphics)
            * 17 : 640 x 480 monochrome (2-color graphics)
            * 18 : 640 x 480 color (16-color graphics)
            * 19 (Default) : 320 x 200 color (256-color graphics)
        """
        sys.stdout.write(f"\x1b[={value}h")


    def reset_mode(self, value):
        """
        Resets the mode by using the same values that set_mode() uses, except for 7, which disables line wrapping.

        :param int value: Value of mode to reset
        """
        sys.stdout.write(f"\x1b[={value}l")


    def wipe(self):
        """
        Cleans off screen of all text. Be warned this also cleans the cachedScreen variable, if needed you may save cachedScreen to another
        variable... It's a double cache how fun!!
        """
        self.cached_screen = ""
        os.system("clear")


# May or may not be moved into a diffrent path at some point
########################################
# LINE
########################################

class Line:
    def __init__(self, cursor):
        """Constructor to initialize object"""
        self.cursor = cursor

    
    def delete(self, clear_type: Optional[str]="currentline"):
        """
        Delete Current Line, From Cursor Down, From Cursor Up, or all.

        :param str clear_type: Diffrent ways to delete text, I.e. "all", "fromcursordown", "fromcursorup", and "currentline", "untilnewline". 
        """
        if clear_type == "all":
            pass

        elif clear_type == "fromcursordown":
            sys.stdout.write("\x1b[0J")
        
        elif clear_type == "fromcursorup":
            sys.stdout.write("\x1b[1J")

        elif clear_type == "currentline":
            sys.stdout.write("\x1b[2K")
    
        # May not ever be added
        elif clear_type == "untilnewline":
            sys.stdout.write("\x1b[K")

        else:
            pass


    def return_line_number(self):
        """
        Gets current line number
        
        :rtype: int
        :return: Returns current line number cursor sits on
        """
        return self.cursor.get_pos("y")


    
