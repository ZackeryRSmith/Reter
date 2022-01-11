########################################
# IMPORTS
########################################

import sys
from typing import Optional
import termios
import tty
import re


########################################
# CURSOR
########################################

class Cursor:
    """
    Terminal cursor.
    """
    def __init__(self, posx, posy, visibility: Optional[bool]=True, blink: Optional[bool]=True):
        """ Constructor to initialize the object
        
        :param int posx: Begining x position for cursor
        :param int posy: Begining y position for cursor
        :param bool visibility: True = Shown, False = Hidden
        
        :: Deprecated
        :param bool blink: True = Cursor blinking, False = No cursor blinking
        """
        self.MEMORY = {}  # An extra place to store some info
        self.posx = posx
        self.posy = posy
        self.visibility = visibility
        self.blink = blink
        if self.visibility:
            self.change_visibility(True)
        else:
            self.change_visibility(False)
 
        ''' Deprecated
        if self.blink:
            self.change_blink(True)
        else:
            self.change_blink(False)
        '''


    def link(self):
        """
        Links cursor object to a screen object. This will auto restrict the cursor to the screen dimensions, if this is not what you are looking
        for set `linkCursor=False` when creating a Screen object!
        """
        pass


    def change_visibility(self, visibility):
        """
        Changes the visibility of cursor

        :param bool visibility: True = Shown, False = Hidden
        """
        self.visibility = visibility
        if self.visibility:
            sys.__stdout__.write("\x1b[?25h")
        else:
            sys.__stdout__.write("\x1b[?25l")


    ''' Deprecated
    def change_blink(self, blink):
        """
        Is currently the same thing as change_visibility(). Just use change_visibility as it is standardized!
        """
        self.visibility = visibility
        if self.visibility:
            sys.__stdout__.write("\x1b[?25h")
        else:
            sys.__stdout__.write("\x1b[?25l")
    '''


    def home(self, universal: Optional[bool]=True):
        """
        Goes to home position
        """
        if universal:
            self.move(0, -1)
        else:
            pass
            #sys.stdout.write("\x1b[H")


    def save_pos(self):
        """
        Gets, and saves the current cursor position. Can later be restored with restore_pos()!
        """
        self.MEMORY.update({"saved_pos":self.get_pos()})


    def restore_pos(self):
        """
        Restores the most recently saved cursor position, saved with save_pos().
        """
        if self.MEMORY != {}:
            self.set_pos(self.MEMORY["saved_pos"][0], self.MEMORY["saved_pos"][1])
        else:
            # No position saved in memory  
            pass


    def get_pos(self, xory: Optional[str]=None, updatePos: Optional[bool]=True):
        """
        Obtains position of cursor. This can be funky on some terminal emulators, for me my daily driver Terminator you must change up some
        settings to get this code to work! This may be the same for your end-user. Make sure you keep this in mind while using get_pos()!
        
        :param str xory: Choose what to return "x", or "y". Default None (Meaning it will return both x and y)
        :param bool updatePos: Auto Updates cursor position after fetching row and col. Default is True

        :rtype: tuple of int's
        :return: Returns (column, row)
        """
        OldStdinMode = termios.tcgetattr(sys.stdin)
        settings = termios.tcgetattr(sys.stdin)
        settings[3] = settings[3] & ~(termios.ECHO | termios.ICANON)  # Disable echo, and stop the terminal from waiting for key press
        termios.tcsetattr(sys.stdin, termios.TCSAFLUSH, settings)
        try:
            temp = ""
            sys.__stdout__.write("\x1b[6n")  # Write mouse position silently
            sys.__stdout__.flush()  # Allows the write() code above this line to be read
            while not (temp := temp + sys.stdin.read(1)).endswith('R'):  # If you are confussed on this look at stackoverflow.com/questions/26000198/what-does-colon-equal-in-python-mean
                pass
            res = re.match(r".*\[(?P<y>\d*);(?P<x>\d*)R", temp)  # Creates groups for values using regex
        finally:
            termios.tcsetattr(sys.stdin, termios.TCSAFLUSH, OldStdinMode)  # Re-enables "echo"
        if res:
            if updatePos:
                self.posx = res.group("x")
                self.posy = res.group("y")
            if xory == None:
                return (int(res.group("x")), int(res.group("y")))  # Returns (x, y)
            elif xory == "x":
                return int(res.group("x"))
            elif xory == "y":
                return int(res.group("y"))
            else:
                # Error class has yet to be added to sub-modules
                #raise IllegalArgumentError('"%s" is an illegal argument!' % (xory) + " Come on dude... it's in the variable name..")
                pass


    def prev_line(self):
        """
        Goes back to previous line, alternatively use move().
        """
        self.move(0, -1)
    

    def next_line(self):
        """
        Goes to next line, alternatively use move().
        """
        self.move(0, 1)


    def set_pos(self, x, y):
        """
        Sets the position of cursor. If you are looking for changing the value and not setting the value look towards .move().

        :param int x: x position to set
        :param int y: y position to set
        """
        self.posx = int(x)
        self.posy = int(y)
        #-- Why do this you may as well it seemed like ESC[#;#H did not work. This did so I just opted for it
        #   If you know the reason or can fix it make a pull request, create an issue under enhancement label
        #   or shoot me an email!
 
        # Get the distance between current postion, and the position to set
        currentPos = self.get_pos()
        self.move(int(x)-int(currentPos[0]), int(y)-int(currentPos[1]))
        #sys.__stdout__.write("\x1b[%s;%sH" % (self.posy, self.posx))


    def return_pos(self, currentPos: Optional[bool]=True):
        """
        Returns cursor position

        :param bool currentPos: If true the current cursor position will be calculated, if false returnPos will take from object (self). Default True
    
        :rtype: tuple of int's
        :return: Returns cursor position saved in object (self) unless currentPos is true. Else current cursor position is calculated then returned
        """
        if currentPos:
            self.get_pos(updatePos=True)  # Gets current cursor position then updates object (self)
        return (self.posx, self.posy)


    def move(self, x, y):
        """
        Changes the position of the cursor. If you are looking to set the value and not change the value look towards .setPos().

        :param int x: x position to change
        :param int y: y position to change
        """
        self.posx = x
        self.posy = y
        # Because of the way ESC[C works 0 must be ignored.. Thus removing elif is not an option.
        if self.posx > 0:  # +
            sys.__stdout__.write('\x1b[%sC' % (self.posx))
        elif self.posx < 0:  # -
            sys.__stdout__.write('\x1b[%sD' % (int(str(self.posx)[1:])))  # Removes negative number with splicing
        
        if self.posy > 0:  # +
            sys.__stdout__.write('\x1b[%sB' % (self.posy))
        elif self.posy < 0:  # -
            sys.__stdout__.write('\x1b[%sA' % (int(str(self.posy)[1:])))  # Removes negative number with splicing
        sys.__stdout__.flush()  # Update line


    def align(self, position):
        """
        Align cursor position with preset position E.g. "left" will put the cursor to the left side. "tright" will place the cursor in the
        top right of the screen

        :param string position: The position to go to I.e. 
                                           "tleft" "tmiddle" "tright"
                                            "left" "middle" "right"
                                           "bleft" "bmiddle" "bright"
        """
        # Align still needs to be finished. With the knowledge and stuff implemented now this can be done right! I will get around to this...
        # That is when I need the cursor.align function..

        if position=="left":
            self.move(-999, 0)
        elif position=="right":
            self.move(999, 0)
