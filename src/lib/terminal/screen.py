########################################
# IMPORTS
########################################

import re
import sys
import os
from typing import Optional
from lib.cursor.cursor import Cursor  


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
        if return_format == "WxH":
            return str(terminal_size.columns)+"x"+str(terminal_size.lines)

        elif return_format == "HxW":
            return str(terminal_size.lines)+"x"+str(terminal_size.columns)
        
        elif return_format == "xy":
            return (terminal_size.columns, terminal_size.lines)
        
        elif return_format == "yx":
            return (terminal_size.lines, terminal_size.columns)
        
        elif return_format == "x":
            return terminal_size.columns
        
        elif return_format == "y":
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

        :param str clear_type: Diffrent ways to delete text, I.e. "all", "fromcursordown", "fromcursorup", and "currentline". 
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
            pass

        else:
            pass


    def return_line_number(self):
        """
        Gets current line number
        
        :rtype: int
        :return: Returns current line number cursor sits on
        """
        return self.cursor.get_pos("y")


    def chunk_it(self, screen, pattern, line_number, max_chunk: Optional[int]=None):
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
        if line_number == None:
            line_number = self.return_line_number()
        try:
            rawValue = screen.cached_screen.split("\n")[lineNumber-1]
        except AttributeError:
            # Fix this error to use custom error handler (/errhandler/)
            sys.exit(indicator.colour.formatting.bold+indicator.colour.formatting.underline+"Hey it seems you did not pass a screen object... You have passed a '%s' object" % (type(screen)))

        # Check for regex
        try:
            # Do some manual checks for re
            if pattern.isspace():
                raise re.error("Intentionaly raised error")
            isRe = re.compile(pattern)
        except re.error:
            isRe = False
        if isRe:
            # Deal with regular expression here
            pass
        else:
            # Uses "".split() to split string (Taking the easy way out.. this code is subject to change!)
            split_value = (raw_value.split(pattern) if max_chunk == None else raw_value.split(pattern, max_chunk))
            # Remove random items and whitspace from splitValue
            remove_space = [x.strip(' ') for x in split_value]
            remove_random = [x for x in remove_space if not x.startswith('\x1b')]
            delete_empty = [item for item in remove_random if item.strip()]
            split_value = delete_empty
            # Convert list of strings to a list of chunk objects
            for index, item in enumerate(split_value):
                # Get positions of items on screen
                for match in re.finditer(split_value[index], raw_value):  # A wee bit of re
                    position = (line_number, match.start(), match.end())
                split_value[index] = Chunk(position, item)
            return split_value


    def remove(self):
        """
        Remove an entire chunk
        """
        pass


# May or may not be removed or put into another path
########################################
# CHUNK
########################################

class Chunk:
    def __init__(self, position, value):
        """Constructor to initialize object"""
        self.value = value
        self.formatting = {}


    def set_colour(self, cursor, fg: Optional[str]=None, bg: Optional[str]=None):
        """
        Sets an entire chunks colour. FG and BG are supported.. additional slots may be added in the future!

        :param object cursor: Cusor object, with a terminal object you can just pass `terminal.cursor`
        :param str fg: Foreground colour
        :param str bg: Background colour
        """
        init_pos = cursor.get_pos() 
        stripped = self.value.rstrip()
        cursor.set_pos(self.position[1]+1, self.position[0]) 
        # stdout.write() issue. https://github.com/ZackeryRSmith/Reter/issues/2
        #sys.stdout.write(("" if fg == None else fg)+("" if bg == None else bg)+stripped+indicator.colour.formatting.eoc)
        print(("" if fg == None else fg)+("" if bg == None else bg)+stripped+indicator.colour.formatting.eoc)
        cursor.set_pos(initPos[0], initPos[1])
        self.formatting.update({
            "colour": {
                "fg":fg,
                "bg":bg
            }
        })


    def set_pos(self):
        """
        """
        pass


    def move(self, cursor, x, y):
        """
        Moves a chunk
        """
        # This should be re-worked. There were quite of weird bugs that should not be overlooked.
        
        # Move cursor to ending chunk position
        cursor.set_pos(self.position[2]+1, self.position[0])
        # Delete chunk
        for i in range(self.position[1], self.position[2]):
            sys.__stdout__.write("\b")
            sys.__stdout__.write(" ")
            sys.__stdout__.write("\b")
        # Move cursor to starting chunk position
        cursor.set_pos(self.position[1]+1, self.position[0])
        # Move cursor to desired position
        print(" " if x > 1 else "", end="")  # If x is bigger then 1 some weird things happen. This fixes it
        cursor.move(x-1, y) if self.position[1] == 0 else cursor.move(x, y)  # Turnary operator fixes some formatting bugs
        # Place chunk
        print(("" if self.formatting["colour"]["fg"] == None else self.formatting["colour"]["fg"])+("" if self.formatting["colour"]["bg"] == None else self.formatting["colour"]["bg"])+self.value.rstrip()+indicator.colour.formatting.eoc)
        # Update self.position
        self.position = (self.position[0]+y, self.position[1]+x, self.position[2]+x)


    def return_value(self):
        """
        Returns value stored in chunk
        """
        return self.value
    

    def return_pos(self):
        """
        Returns position of value stored in chunk
        
        :rtype: tuple of int's
        :return: Returns (starting_char_position, ending_char_position, line_number)
        """
        return self.position

    
